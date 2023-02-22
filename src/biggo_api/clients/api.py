"""This module define a general api client contains clients for instances"""

from biggo_api._auth import auth_client_credentials
from biggo_api.clients.comment import CommentClient
from biggo_api.clients.user import UserClient
from biggo_api.clients.video import VideoClient

class APIClient:
    """The API Client wraps all types of client

    This client creates only 1 oauth2 session for all clients.

    Attributes:
        comment: See `biggo_api.clients.comment.CommentClient`
        user: See `biggo_api.clients.user.UserClient`
        video: See `biggo_api.clients.video.VideoClient`
    """
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        host_url: str = 'https://api.biggo.com',
        verify: bool = True,
        **kwargs,
    ):
        oauth2_session = auth_client_credentials(
            url='/'.join([host_url, 'auth/v1/token']),
            client_id=client_id, client_secret=client_secret,
            verify=verify,
            refresh_url='/'.join([host_url, 'auth/v1/refresh_token']),
        )
        params = {
            'oauth2_session': oauth2_session,
            'host_url': host_url,
            'verify': verify,
        } | kwargs
        self.comment = CommentClient(**params)
        self.user = UserClient(**params)
        self.video = VideoClient(**params)
        pass
    pass
