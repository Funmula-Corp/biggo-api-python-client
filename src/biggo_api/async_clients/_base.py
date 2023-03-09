"""This module define asynchronous Base Instance Client of BigGo API."""

from json import JSONDecodeError
from logging import getLogger
from typing import Optional

from aiohttp import ClientResponseError
from async_oauthlib.oauth2_session import OAuth2Session

from biggo_api.exception import BigGoAPIError
from biggo_api.responses import ErrorResponse


logger = getLogger(__name__)


class BaseInstanceClient:
    """Base class of Async BigGo API Instance Client.

    BigGo API Client using OAuth 2.0 (https://oauth.net/2/).

    Attributes:
        oauth2_session: An authorized `OAuth2Session` object.
        host_url: API host.
        region: Region of client.
        verify_ssl: Verify SSL certificate.
    """

    def __init__(
        self,
        oauth2_session: OAuth2Session,
        host_url: str,
        verify_ssl: bool,
        region: Optional[str] = None,
    ):
        self.__host_url = host_url
        self.__api_path = 'api/v1'
        self.region = region
        self.verify_ssl = verify_ssl

        # check if oauth2_session exist and authorized
        if not (isinstance(oauth2_session, OAuth2Session) and oauth2_session.authorized):
            raise ValueError("Invalid oauth2_session")
        self.__oauth2_session = oauth2_session
        pass

    async def request(self, method: str, path: str, headers: dict = {}, **kwargs) -> dict:
        """Send request asynchronously to /api/v1/{path} using given method, headers and other keyword arguments.

        Args:
            method: The method of this request.
            path: The sub path of request url.

        Raises:
            BigGoAPIError(response status 4xx, error in response body): Client error.
            ClientResponseError(response status 4xx or 5xx): Parse failed client error or server error.
            ClientResponseError(response status 2xx or 3xx): Result in response body is False.

        Examples:
            Send a GET request to 'https://api.biggo.com/api/v1/example'.

            >>> await client.request(method='GET', path='example')
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
            'verify_ssl': self.verify_ssl,
            'headers': headers,
            **kwargs,
        }
        result = await self.__oauth2_session.request(**params)
        async with result as response:
            content = await response.text()
            logger.debug('status: %s, content: %s', response.status, content)
            try:
                # get parsed response
                response_json: dict = await response.json()
                if response_json.get('result', False):
                    # return parsed response if result = True
                    return response_json
            except JSONDecodeError:
                logger.warning("unable to parse API response: %s", content)
                pass
            pass
            # check if response status is client error with error message
            if 400 <= response.status < 500:
                try:
                    error_response = ErrorResponse.parse_raw(content)
                except BigGoAPIError:
                    pass
                except Exception:
                    logger.warning(
                        "unable to parse 4xx API error: %s", content,
                    )
                    pass
                finally:
                    raise BigGoAPIError(response=error_response)
                pass
            # raise server error if status code = 5xx
            response.raise_for_status()
            # raise ClientResponseError when status code is not 4xx or 5xx but result = False
            raise ClientResponseError(
                request_info=response.request_info,
                history=response.history,
                status=response.status,
                message=f'status is {response.status} but result is False',
                headers=response.headers,
            )
    pass
