"""The API client of video"""

from logging import getLogger
from os import stat
from typing import Optional

from biggo_api.clients._base import BaseInstanceClient
from biggo_api.model import VideoSettings, VideoSettings, UserResponse, VideoResponse, VideoAnalysis


logger = getLogger(__name__)


class VideoClient(BaseInstanceClient):
    """Client to access video API"""

    def has_permission(self) -> bool:
        """
        Verify permission of client to upload video

        Returns:
            A bool value represents result
        """
        response_json = self.request(
            method='POST',
            path='video_auth/self',
        )
        return response_json is not None

    def upload(self, file: str) -> str:
        """Upload video from local file

        Args:
            file: The file path & name of video file

        Returns:
            A str value represents the id of uploaded video
        """
        file_stat = stat(file)
        file_size = file_stat.st_size
        with open(file, 'rb') as video_file:
            response_json = self.request(
                method='POST',
                path='video/',
                files={'video': video_file},
                headers={'File-Size': f'{file_size}'},
            )
            pass
        return response_json['video_id']

    def search(self, keyword: str, tag_only: bool = False) -> list[VideoResponse]:
        """Search videos by keyword or tag

        Args:
            keyword: The keyword to search for
            tag_only: Set to True will search #target

        Returns:
            A list of `biggo_api.model.Video` object
        """
        raise NotImplementedError
        params = {'tag': keyword} if tag_only else {'q': keyword}
        response_json = self.request(
            method='GET',
            path='video/search',
            params=params,
        )
        videos = [
            VideoResponse.from_dict(video)
            for video in response_json['data']
        ]
        return videos

    def recommend(self) -> list[VideoResponse]:
        """Get recommended videos

        Returns:
            A list of `biggo_api.model.Video` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path='video/recommend',
        )
        videos = [
            VideoResponse.from_dict(video)
            for video in response_json['data']
        ]
        return videos

    def get(self, video_id: str) -> Optional[VideoResponse]:
        """Get video

        Args:
            video_id: The id of video

        Returns:
            A `biggo_api.model.Video` object, None if not found
        """
        response_json = self.request(
            method='GET',
            path=f'video/{video_id}',
        )
        if response_json['video']:
            video = VideoResponse.from_dict(response_json['video'][0])
            return video
        return None

    def post_settings(self, video_settings: VideoSettings) -> bool:
        """
        Update video settings using POST method.

        Args:
            video: The `biggo_api.model.VideoSettings` object

        Returns:
            A bool value represents result
        """
        video_settings_dict = video_settings.to_dict(exclude_none=False)
        if None in video_settings_dict.values():
            return False
        response_json = self.request(
            method='POST',
            path=f'video/{video_settings.video_id}',
            json=video_settings_dict,
        )
        return response_json is not None

    def patch_settings(self, video_settings: VideoSettings) -> bool:
        """
        Update video settings using PATCH method

        Args:
            video: The `biggo_api.model.VideoSettings` object

        Returns:
            A bool value represents result
        """
        video_settings_dict = video_settings.to_dict()
        if not video_settings_dict:
            return False
        response_json = self.request(
            method='PATCH',
            path=f'video/{video_settings.video_id}',
            json=video_settings_dict,
        )
        return response_json is not None

    def delete(self, video_id: str) -> bool:
        """Delete video

        Args:
            video_id: The id of video

        Returns:
            A bool value represents result
        """
        response_json = self.request(
            method='DELETE',
            path=f'video/{video_id}',
        )
        return response_json is not None

    def get_like_list(self, video_id: str) -> list[UserResponse]:
        """Get like list of video

        Args:
            video_id: The id of video

        Returns:
            A list of `biggo_api.model.User` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'video/{video_id}/like',
        )
        like_list = [
            UserResponse.from_dict(user)
            for user in response_json['users']
        ]
        return like_list

    def like(self, video_id: str) -> bool:
        """Like video

        Args:
            video_id: The id of video

        Returns:
            A bool value represents result
        """
        raise NotImplementedError
        response_json = self.request(
            method='POST',
            path=f'video/{video_id}/like',
        )
        return response_json is not None

    def unlike(self, video_id: str) -> bool:
        """Unlike video

        Args:
            video_id: The id of video

        Returns:
            A bool value represents result
        """
        raise NotImplementedError
        response_json = self.request(
            method='DELETE',
            path=f'video/{video_id}/like',
        )
        return response_json is not None

    def analyze(self, video_id: str) -> VideoAnalysis:
        """Get video analyzation

        Args:
            video_id: The id of video

        Returns:
            A `biggo_api.model.VideoAnalysis` object
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'video/{video_id}/analyze',
        )
        analysis = VideoAnalysis.from_dict(response_json['data'])
        return analysis
    pass
