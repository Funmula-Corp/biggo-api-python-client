"""The API client of user"""

from biggo_api.clients._base import BaseClient
from biggo_api.model import Product, User, Video


class UserClient(BaseClient):
    """Client to access user API"""

    def get_subscribed_video_list(self, user_id: str) -> list[Video]:
        """Get videos from user's subscribed accounts

        Args:
            user_id: The id of user

        Returns:
            A list of `biggo_api.model.Video` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/video_subscribed/',
        )
        subscribed_videos = [
            Video.from_dict(video)
            for video in response_json['video_subscribed']['data']
        ]
        return subscribed_videos

    def get_favorite_product_list(self, user_id: str) -> list[Product]:
        """Get user's favorite products

        Args:
            user_id: The id of user

        Returns:
            A list of `biggo_api.model.Product` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/subscribe_product/',
        )
        subscribe_products = [
            Product.from_dict(product)
            for product in response_json['subscribe_product']['data']
        ]
        return subscribe_products

    def get_liked_video_list(self, user_id: str) -> list[Video]:
        """Get liked videos

        Args:
            user_id: The id of user

        Returns:
            A list of `biggo_api.model.Video` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/like_video/',
        )
        liked_videos = [
            Video.from_dict(video)
            for video in response_json['like_video']['data']
        ]
        return liked_videos

    def get_public_video_list(self, user_id: str) -> list[Video]:
        """Get user's public videos

        Args:
            user_id: The id of user

        Returns:
            A list of `biggo_api.model.Video` objects
        """
        params = {
            'tab': 'user_video',
        }
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/video/',
            params=params,
        )
        user_videos = [
            Video.from_dict(video)
            for video in response_json['user_video']['data']
        ]
        return user_videos

    def get_own_video_list(self) -> list[Video]:
        """Get client's own videos

        Returns:
            A list of `biggo_api.model.Video` objects
        """
        params = {
            'tab': 'user_video',
        }
        response_json = self.request(
            method='GET',
            path='user/self/video/',
            params=params,
        )
        user_videos = [
            Video.from_dict(video)
            for video in response_json['user_video']['data']
        ]
        return user_videos

    def follow(self, user_id: str) -> bool:
        """Follow user

        Args:
            user_id: The id of user

        Returns:
            A bool value represents result
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

        Returns:
            A bool value represents result
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

        Returns:
            A bool value represents result
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

        Returns:
            A bool value represents result
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

        Returns:
            A bool value represents result
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

        Returns:
            A bool value represents result
        """
        raise NotImplementedError
        response_json = self.request(
            method='DELETE',
            path=f'user/{user_id}/block',
        )
        return response_json is not None

    def get_block_list(self, user_id: str) -> list[User]:
        """Get block list

        Args:
            user_id: The id of user

        Returns:
            A list of `biggo_api.model.User` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/block',
        )
        block_list = [
            User.from_dict(user)
            for user in response_json['block_list']
        ]
        return block_list

    def get_follower_count(self, user_id: str) -> int:
        """Get follower count

        Args:
            user_id: The id of user

        Returns:
            An int value represents number of followers
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/follower_amount',
        )
        return response_json['follower_count']

    def get_follow_user_list(self, user_id: str) -> list[User]:
        """Get following users

        Args:
            user_id: The id of user

        Returns:
            A list of `biggo_api.model.User` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/follower',
        )
        follow_users = [
            User.from_dict(user)
            for user in response_json['follow_user']
        ]
        return follow_users

    def get_follower_list(self, user_id: str) -> list[User]:
        """Get followed users

        Args:
            user_id: The id of user

        Returns:
            A list of `biggo_api.model.User` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'user/{user_id}/follow',
        )
        followers = [
            User.from_dict(user)
            for user in response_json['follower']
        ]
        return followers
    pass
