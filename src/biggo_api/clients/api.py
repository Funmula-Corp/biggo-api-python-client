"""This module define a general api client contains clients of instances."""

from logging import getLogger
from typing import Optional

from biggo_api.clients._auth import ClientCredentials, auth_client_credentials
from biggo_api.clients._user import UserClient
from biggo_api.clients._video import VideoClient


logger = getLogger(__name__)


class APIClient:
    """The API client wraps all types of clients.

    The API client will be authorized using given grant type.

    Attributes:
        params: Parameters of API client, including oauth_session, host_url, region and verify.
        user: User client.
        video: Video client.
    """
    user: UserClient
    video: VideoClient

    def __init__(
        self,
        client_credentials: Optional[ClientCredentials],
        host_url: str = 'https://api.biggo.com',
        region: Optional[str] = None,
        verify: bool = True,
        **kwargs,
    ):
        """Authorize client using given grant type."""
        # check if client_credentials is provided
        if client_credentials is not None:
            oauth2_session = auth_client_credentials(
                url='/'.join([host_url, 'auth/v1/token']),
                client_credentials=client_credentials,
                verify=verify,
                refresh_url='/'.join([host_url, 'auth/v1/token']),
            )
            pass
        # no other OAuth 2.0 grant types
        else:
            raise ValueError("Missing parameters for authorization.")

        self.params = {
            'oauth2_session': oauth2_session,
            'host_url': host_url,
            'region': region,
            'verify': verify,
        }
        # initialized user client
        self.user = UserClient(**self.params)
        # initialized video client
        self.video = VideoClient(**self.params)

        if kwargs:
            logger.warning("ignoring kwargs: %s", kwargs)
            pass
        pass
    pass
