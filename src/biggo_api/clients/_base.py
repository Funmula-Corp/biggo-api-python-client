"""Base Instance API Client"""

from logging import getLogger
from typing import Optional

from requests.exceptions import HTTPError
from requests_oauthlib import OAuth2Session

from biggo_api._auth import auth_client_credentials
from biggo_api.exception import BigGoAPIException


logger = getLogger(__name__)


class BaseClient:
    """Base class of BigGo API Client

    BigGo API Client using OAuth 2.0 (https://oauth.net/2/).

    Support grant types & required parameters:
    - Client Credentials:
        - client_id
        - client_secret
    """

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        oauth2_session: Optional[OAuth2Session] = None,
        host_url: str = 'https://api.biggo.com',
        verify: bool = True,
        **kwargs,
    ):
        """Construct Client

        Args:
            client_id: id for authentication
            client_secret: secret for authentication
            oauth2_session: An authorized `requests_oauthlib.OAuth2Session` object
            host_url: api host
            verify: Verify SSL certificate
        """
        self.__host_url = host_url
        self.__api_path = 'api/v1'
        self.verify = verify

        self.__oauth2_session = oauth2_session
        if self.__oauth2_session is not None and self.__oauth2_session.authorized:
            logger.info("passing authorized oauth2 session")
            pass
        # check if client_id and client_secret provided
        elif client_id and client_secret:
            # authorized with client credential grant
            self.__oauth2_session = auth_client_credentials(
                url='/'.join([self.__host_url, 'auth/v1/token']),
                client_id=client_id, client_secret=client_secret,
                verify=verify,
                refresh_url='/'.join([self.__host_url, 'auth/v1/refresh_token']),
            )
            logger.info("authorized by client credentials")
            pass
        else:
            raise BigGoAPIException(code=2, message="Without access token.")
        if kwargs:
            logger.warning("ignoring keyword arguments: %s", kwargs)
            pass
        pass

    def request(self, method: str, path: str, **kwargs) -> dict:
        """Send request to /api/v1/{path} using given method with keyword arguments

        Args:
            method: The method of this request
            path: The sub path of request url after {host}/{api_path}

        Returns:
            A dict object (parsed response)
        """
        # compose request url in the format: {host_url}/{api_path}/{path}
        url = '/'.join([self.__host_url, self.__api_path, path])
        # setup parameters that sent to request function
        params = {
            'method': method,
            'url': url,
            'verify': self.verify,
            **kwargs,
        }
        response = self.__oauth2_session.request(**params)
        logger.debug(
            'status: %s, content: %s',
            response.status_code, response.content,
        )
        response_json: dict = response.json()
        if response_json.get('result', False):
            return response_json
        if (
            400 <= response.status_code < 500 and
            'error' in response_json and
            'message' in response_json['error']
        ):
            raise BigGoAPIException(**response_json['error'])
        response.raise_for_status()
        raise HTTPError(
            f'{response.status_code} Result equals False',
            response=response,
        )

    @property
    def authorized(self) -> bool:
        """Check client authorization status

        Returns:
            A bool value represents authorization status. True if authorized, otherwise False.
        """
        if self.__oauth2_session:
            return self.__oauth2_session.authorized
        logger.warning("OAuth2Session undefined")
        return False
    pass
