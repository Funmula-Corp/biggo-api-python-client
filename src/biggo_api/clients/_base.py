"""This module define Base Instance Client of BigGo API."""

from logging import getLogger
from typing import Optional

from pydantic import ValidationError
from requests.exceptions import HTTPError
from requests_oauthlib import OAuth2Session

from biggo_api.exception import BigGoAPIError
from biggo_api.responses import ErrorResponse


logger = getLogger(__name__)


class BaseInstanceClient:
    """Base class of BigGo API Instance Client.

    BigGo API Client using OAuth 2.0 (https://oauth.net/2/).

    Attributes:
        oauth2_session: An authorized `OAuth2Session` object.
        host_url: API host.
        region: Region of client.
        verify: Verify SSL certificate.
    """

    def __init__(
        self,
        oauth2_session: OAuth2Session,
        host_url: str,
        verify: bool,
        region: Optional[str] = None,
    ):
        self.__host_url = host_url
        self.__api_path = 'api/v1'
        self.region = region
        self.verify = verify

        # check if oauth2_session exist and authorized
        if not (isinstance(oauth2_session, OAuth2Session) and oauth2_session.authorized):
            raise ValueError("Invalid oauth2_session")
        self.__oauth2_session = oauth2_session
        pass

    def request(self, method: str, path: str, headers: dict = {}, **kwargs) -> dict:
        """Send request to /api/v1/{path} using given method, headers and other keyword arguments.

        Args:
            method: The method of this request.
            path: The sub path of request url.

        Raises:
            BigGoAPIError(response status 4xx, error in response body): Client error.
            HTTPError(response status 4xx or 5xx): Client(rarely) or server error.
            HTTPError(response status 2xx or 3xx): Result in response body is False.

        Examples:
            Send a GET request to 'https://api.biggo.com/api/v1/example'.

            >>> client.request(method='GET', path='example')
            { "result": True, ... }
        """
        # compose request url in the format: {host_url}/{api_path}/{path}
        url = '/'.join([self.__host_url, self.__api_path, path])
        # add region to header if provided
        if self.region is not None:
            headers = {'region': self.region} | headers
            pass
        # set request parameters
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
        # get parsed response
        response_json: dict = response.json()
        if response_json.get('result', False):
            # return parsed response if result = True
            return response_json
        # check if response status is client error with error message
        if 400 <= response.status_code < 500:
            try:
                error_response = ErrorResponse.parse_obj(response_json)
                raise BigGoAPIError(response=error_response)
            except ValidationError as ex:
                logger.warning(
                    "unable to parse 4xx API error: %s", response_json,
                )
                pass
            pass
        # raise server error if status code = 5xx
        response.raise_for_status()
        # raise HTTPError when status code is not 4xx or 5xx but result = False
        raise HTTPError(
            f'status is {response.status_code} but result is False',
            response=response,
        )
    pass
