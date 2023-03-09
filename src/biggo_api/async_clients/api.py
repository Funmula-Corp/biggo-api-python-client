"""This module define a general async api client contains async clients of instances."""

from logging import getLogger
from typing import Optional

from async_oauthlib.oauth2_session import OAuth2Session

from biggo_api.async_clients._auth import ClientCredentials, auth_client_credentials
from biggo_api.async_clients._user import UserClient
from biggo_api.async_clients._video import VideoClient


logger = getLogger(__name__)


class APIClient:
    """The async API client wraps all types of async clients.

    The API client will be authorized by passing grant type into `authorize` method.

    Attributes:
        params: Parameters of API client, including oauth_session, host_url, region and verify_ssl.
        user: User client.
        video: Video client.
    """
    params: dict = {}
    user: UserClient = None
    video: VideoClient = None

    def __init__(
        self,
        host_url: str = 'https://api.biggo.com',
        region: Optional[str] = None,
        verify_ssl: bool = True,
        **kwargs,
    ):
        self.params = {
            'oauth2_session': None,
            'host_url': host_url,
            'region': region,
            'verify_ssl': verify_ssl,
        }

        if kwargs:
            logger.warning("ignoring kwargs: %s", kwargs)
            pass
        pass

    async def authorize(
        self,
        client_credentials: Optional[ClientCredentials],
    ):
        """Authorize client asynchronously using given grant type.

        Args:
            client_credentials: Parameters for client credentials grant type.

        Examples:
            >>> client_credentials = ClientCredentials(
            ...     client_id='CLIENT_ID', client_secret='CLIENT_SECRET',
            ... )
            >>> api_client = APIClient()
            >>> await api_client.authorize(client_credentials=client_credentials)
        """
        host_url = self.params['host_url']
        verify_ssl = self.params['verify_ssl']
        # check if client_credentials is provided
        if client_credentials is not None:
            oauth2_session = await auth_client_credentials(
                url='/'.join([host_url, 'auth/v1/token']),
                client_credentials=client_credentials,
                verify_ssl=verify_ssl,
                refresh_url='/'.join([host_url, 'auth/v1/token']),
            )
            pass
        # no other OAuth 2.0 grant types
        else:
            raise ValueError("Missing parameters for authorization.")

        self.params['oauth2_session'] = oauth2_session

        # initialized user client
        self.user = UserClient(**self.params)
        # initialized video client
        self.video = VideoClient(**self.params)
        pass

    async def close(self):
        """Close OAuth2Session.

        Examples:
            >>> await api_client.close()
        """
        session: OAuth2Session = self.params['oauth2_session']
        await session.close()
        pass
    pass
