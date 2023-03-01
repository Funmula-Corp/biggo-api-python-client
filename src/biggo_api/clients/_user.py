"""The API client of user"""

from biggo_api.clients._base import BaseInstanceClient
from biggo_api.model import ProductResponse, UserResponse, VideoResponse


class UserClient(BaseInstanceClient):
    """Client to access user API"""

    def get_subscribed_video_list(self, user_id: str) -> list[VideoResponse]:
        """Get videos from user's subscribed accounts

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/video_subscribed/',
        )
        subscribed_videos = [
            VideoResponse.from_dict(video)
            for video in response_json['video_subscribed']['data']
        ]
        return subscribed_videos

    def get_favorite_product_list(self, user_id: str) -> list[ProductResponse]:
        """Get user's favorite products

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/subscribe_product/',
        )
        subscribe_products = [
            ProductResponse.from_dict(product)
            for product in response_json['subscribe_product']['data']
        ]
        return subscribe_products

    def get_liked_video_list(self, user_id: str) -> list[VideoResponse]:
        """Get liked videos

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/like_video/',
        )
        liked_videos = [
            VideoResponse.from_dict(video)
            for video in response_json['like_video']['data']
        ]
        return liked_videos

    def get_user_video_list(self, user_id: str) -> list[VideoResponse]:
        """Get user's videos

        Args:
            user_id: The id of user
        """
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/video/',
        )
        user_videos = [
            VideoResponse.from_dict(video)
            for video in response_json['user_video']['data']
        ]
        return user_videos

    def get_own_video_list(self) -> list[VideoResponse]:
        """Get client's own videos
        """
        response_json = self.request(
            method='GET',
            path='user/self/video/',
        )
        user_videos = [
            VideoResponse.from_dict(video)
            for video in response_json['user_video']['data']
        ]
        return user_videos

    def follow(self, user_id: str) -> bool:
        """Follow user

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='POST',
            path=f'user/{user_id}/follow',
        )
        return response_json is not None

    def unfollow(self, user_id: str) -> bool:
        """Unfollow user

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='DELETE',
            path=f'user/{user_id}/follow',
        )
        return response_json is not None

    def remove_follower(self, follower_id: str):
        """Unfollow user

        Args:
            follower_id: The user id of follower
        """
        raise NotImplementedError
        response_json = self.request(
            method='DELETE',
            path=f'user/{follower_id}/follow',
        )
        return response_json is not None

    def is_following(self, user_id: str) -> bool:
        """Check if following user

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/follow',
        )
        return response_json['is_follow']

    def block(self, user_id: str) -> bool:
        """Block user

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='POST',
            path=f'user/{user_id}/block',
        )
        return response_json is not None

    def unblock(self, user_id: str) -> bool:
        """Unblock user

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='DELETE',
            path=f'user/{user_id}/block',
        )
        return response_json is not None

    def get_block_list(self, user_id: str) -> list[UserResponse]:
        """Get block list

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/block',
        )
        block_list = [
            UserResponse.from_dict(user)
            for user in response_json['block_list']
        ]
        return block_list

    def get_follower_count(self, user_id: str) -> int:
        """Get follower count

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/follower_amount',
        )
        return response_json['follower_count']

    def get_follow_user_list(self, user_id: str) -> list[UserResponse]:
        """Get following users

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/follower',
        )
        follow_users = [
            UserResponse.from_dict(user)
            for user in response_json['follow_user']
        ]
        return follow_users

    def get_follower_list(self, user_id: str) -> list[UserResponse]:
        """Get followed users

        Args:
            user_id: The id of user
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/follow',
        )
        followers = [
            UserResponse.from_dict(user)
            for user in response_json['follower']
        ]
        return followers
    pass
