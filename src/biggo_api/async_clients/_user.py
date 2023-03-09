"""The asynchronous API client of user."""

from biggo_api.async_clients._base import BaseInstanceClient
from biggo_api.responses import UserVideoResponse


class UserClient(BaseInstanceClient):
    """Async client to access user API."""

    async def get_user_videos(self, userid: str, page: int = 1) -> UserVideoResponse:
        """Get user's videos asynchronously.

        Args:
            user_id: The id of user.
            page: The page of user videos. (20 videos in one page)

        Examples:
            Assume user has 22 videos, get videos from page 1 to page 3.

            >>> await user_client.get_user_videos(userid='USERID', page=1)
            UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...), ...], size=22))
            >>> await user_client.get_user_videos(userid='USERID', page=2)
            UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...)], size=22))
            >>> await user_client.get_user_videos(userid='USERID', page=3)
            UserVideoResponse(result=True, user_video=UserVideo(data=[], size=22))
        """
        response_json = await self.request(
            method='GET',
            path=f'user/{userid}/video/',
            params={'p': page},
        )
        return UserVideoResponse.parse_obj(response_json)

    async def get_own_videos(self, page: int = 1) -> UserVideoResponse:
        """Get client's own videos asynchronously.

        Args:
            page: The page of user videos. (20 videos in one page)

        Examples:
            Assume user has 22 videos, get videos from page 1 to page 3.

            >>> await user_client.get_user_videos(page=1)
            UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...), ...], size=22))
            >>> await user_client.get_user_videos(page=2)
            UserVideoResponse(result=True, user_video=UserVideo(data=[BigGoVideo(...), BigGoVideo(...)], size=22))
            >>> await user_client.get_user_videos(page=3)
            UserVideoResponse(result=True, user_video=UserVideo(data=[], size=22))
        """
        response_json = await self.request(
            method='GET',
            path='user/self/video/',
            params={'p': page},
        )
        return UserVideoResponse.parse_obj(response_json)
    pass
