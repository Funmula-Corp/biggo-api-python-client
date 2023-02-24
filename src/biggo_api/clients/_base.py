"""Base API Instance Client"""

from logging import getLogger
from typing import Optional

from requests.exceptions import HTTPError
from requests_oauthlib import OAuth2Session

from biggo_api.exception import BigGoAPIException


logger = getLogger(__name__)


class BaseInstanceClient:
    """Base class of BigGo API Instance Client

    BigGo API Client using OAuth 2.0 (https://oauth.net/2/).

    Support grant types & required parameters:
    - Client Credentials:
        - client_id
        - client_secret
    """

    def __init__(
        self,
        oauth2_session: OAuth2Session,
        host_url: str,
        verify: bool,
        region: Optional[str] = None,
    ):
        """Construct Client

        Args:
            client_id: Id for authentication
            client_secret: Secret for authentication
            oauth2_session: An authorized `requests_oauthlib.OAuth2Session` object
            host_url: API host
            region: Region of client, leave it `None` will auto filled by server
            verify: Verify SSL certificate
        """
        self.__host_url = host_url
        self.__api_path = 'api/v1'
        self.region = region
        self.verify = verify

        if not (isinstance(oauth2_session, OAuth2Session) and oauth2_session.authorized):
            raise ValueError("Invalid oauth2_session")
        self.__oauth2_session = oauth2_session
        pass

    def request(self, method: str, path: str, headers: dict = {}, **kwargs) -> dict:
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
        if self.region is not None:
            headers = {'region': self.region} | headers
            pass
        params = {
            'method': method,
            'url': url,
            'verify': self.verify,
            'headers': headers,
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
    pass
