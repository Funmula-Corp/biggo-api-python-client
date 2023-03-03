"""The API client of user."""

from biggo_api.clients._base import BaseInstanceClient
from biggo_api.responses import UserVideoResponse


class UserClient(BaseInstanceClient):
    """Client to access user API."""

    def get_user_videos(self, userid: str) -> UserVideoResponse:
        """Get user's videos

        Args:
            user_id: The id of user
        """
        response_json = self.request(
            method='GET',
            path=f'user/{userid}/video/',
        )
        return UserVideoResponse.parse_obj(response_json)

    def get_own_videos(self) -> UserVideoResponse:
        """Get client's own videos"""
        response_json = self.request(
            method='GET',
            path='user/self/video/',
        )
        return UserVideoResponse.parse_obj(response_json)
    pass
