"""This module define a general api client contains clients for instances"""

from logging import getLogger
from typing import Optional

from biggo_api.clients._auth import ClientCredentials, auth_client_credentials
from biggo_api.clients._comment import CommentClient
from biggo_api.clients._user import UserClient
from biggo_api.clients._video import VideoClient


logger = getLogger(__name__)


class APIClient:
    """The API Client wraps all types of client

    Attributes:
        comment: See `biggo_api.clients.comment.CommentClient`
        user: See `biggo_api.clients.user.UserClient`
        video: See `biggo_api.clients.video.VideoClient`
    """
    def __init__(
        self,
        client_credentials: Optional[ClientCredentials],
        host_url: str = 'https://api.biggo.com',
        region: Optional[str] = None,
        verify: bool = True,
        **kwargs,
    ):
        """Initialize API Client"""
        if client_credentials is not None:
            oauth2_session = auth_client_credentials(
                url='/'.join([host_url, 'auth/v1/token']),
                client_credentials=client_credentials,
                verify=verify,
                refresh_url='/'.join([host_url, 'auth/refresh_token']),
            )
            pass
        else:
            raise ValueError("Please supply either code or authorization_response parameters.")
        params = {
            'oauth2_session': oauth2_session,
            'host_url': host_url,
            'region': region,
            'verify': verify,
        }
        self.comment = CommentClient(**params)
        self.user = UserClient(**params)
        self.video = VideoClient(**params)
        if kwargs:
            logger.warning("ignoring kwargs: %s", kwargs)
            pass
        pass
    pass
