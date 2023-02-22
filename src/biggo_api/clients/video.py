"""The API client of video"""

from logging import getLogger
from os import stat
from typing import Optional

from biggo_api.clients._base import BaseClient
from biggo_api.model import EditedVideo, NewVideo, User, Video, VideoAnalysis


logger = getLogger(__name__)


class VideoClient(BaseClient):
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

    def search(self, keyword: str, tag_only: bool = False) -> list[Video]:
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
            Video.from_dict(video)
            for video in response_json['data']
        ]
        return videos

    def recommend(self) -> list[Video]:
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
            Video.from_dict(video)
            for video in response_json['data']
        ]
        return videos

    def get(self, video_id: str) -> Optional[Video]:
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
            video = Video.from_dict(response_json['video'][0])
            return video
        return None

    def update(self, edited_video: EditedVideo) -> bool:
        """
        Update video settings

        Args:
            video: The `biggo_api.model.EditedVideo` object

        Returns:
            A bool value represents result
        """
        video_setting = edited_video.to_dict()
        if not video_setting:
            return False
        response_json = self.request(
            method='PATCH',
            path=f'video/{edited_video.video_id}',
            json=video_setting,
        )
        return response_json is not None

    def setup_new_video(self, new_video: NewVideo) -> bool:
        """Setup newly uploaded video

        Args:
            new_video: The `biggo_api.model.NewVideo` object

        Returns:
            A bool value represents result
        """
        response_json = self.request(
            method='POST',
            path=f'video/{new_video.video_id}',
            json=new_video.to_dict(),
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

    def get_like_list(self, video_id: str) -> list[User]:
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
            User.from_dict(user)
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

    def get_follower_liked_videos(self, video_id: str) -> list[Video]:
        """Get for cache

        Args:
            video_id: The id of video
        """
        raise NotImplementedError
        response_json = self.request(
            method='GET',
            path=f'video/{video_id}/follow',
        )
        pass
    pass
