"""Base API Client"""

from logging import getLogger

from oauthlib.oauth2 import BackendApplicationClient
from requests.exceptions import HTTPError
from requests_oauthlib import OAuth2Session

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
        client_id: str,
        client_secret: str,
        host_url: str = 'https://api.biggo.com',
        verify: bool = True,
        **kwargs,
    ):
        """Construct Client

        Args:
            client_id: id for authentication
            client_secret: secret for authentication
            host_url: api host
            verify: Verify SSL certificate
        """
        self.__host_url = host_url
        self.__auth_path = 'auth/v1'
        self.__api_path = 'api/v1'
        self.verify = verify

        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__oauth: OAuth2Session = None

        # check if client_id and client_secret provided
        if client_id and client_secret:
            # authorized with client credential grant
            self.__auth_client_credentials()
            pass
        if kwargs:
            logger.warning("ignoring keyword arguments: %s", kwargs)
            pass
        pass

    def __auth_client_credentials(self) -> None:
        """Authorize by client credentials

        Raises:
            InvalidClientIdError: authorization failed
        """
        # compose refresh token url
        refresh_url = '/'.join(
            [self.__host_url, self.__auth_path, 'refresh_token'],
        )
        # init oauth 2.0 session
        self.__oauth = OAuth2Session(
            client=BackendApplicationClient(client_id=self.__client_id),
            auto_refresh_url=refresh_url,
        )
        # compose token url in the format: {host_url}/{auth_path}/token
        url = '/'.join([self.__host_url, self.__auth_path, 'token'])
        # setup params: token url, auth(id & secret)
        params = {
            'token_url': url,
            'auth': (self.__client_id, self.__client_secret),
            'verify': self.verify,
        }
        # get access token from authorized server
        self.__oauth.fetch_token(**params)
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
        response = self.__oauth.request(**params)
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
        if self.__oauth:
            return self.__oauth.authorized
        logger.warning("OAuth2Session undefined")
        return False
    pass
