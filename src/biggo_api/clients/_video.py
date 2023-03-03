"""The API client of video."""

from json import loads
from logging import getLogger
from os import stat

from biggo_api.clients._base import BaseInstanceClient
from biggo_api.data_models.video import VideoParams
from biggo_api.responses import (
    BaseResponse,
    VideoPermissionResponse,
    VideoResponse,
    VideoUpdateResponse,
    VideoUploadResponse,
)


logger = getLogger(__name__)


class VideoClient(BaseInstanceClient):
    """Client to access video API."""

    def has_permission(self) -> VideoPermissionResponse:
        """Verify permission of client to upload video."""
        response_json = self.request(
            method='POST',
            path='video_auth/self',
        )
        return VideoPermissionResponse.parse_obj(response_json)

    def upload(self, file: str) -> VideoUploadResponse:
        """Upload video from local file.

        Args:
            file: The file path & name of video file.
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
        return VideoUploadResponse.parse_obj(response_json)

    def get(self, video_id: str) -> VideoResponse:
        """Get video.

        Args:
            video_id: The id of video.
        """
        response_json = self.request(
            method='GET',
            path=f'video/{video_id}',
        )
        return VideoResponse.parse_obj(response_json)

    def post_video_params(self, video_params: VideoParams) -> VideoUpdateResponse:
        """Update video parameters using POST method.

        Args:
            video_params: Parameters of video.
        """
        video_params_dict: dict = loads(video_params.json(exclude={'video_id'}))
        response_json = self.request(
            method='POST',
            path=f'video/{video_params.video_id}',
            json=video_params_dict,
        )
        return VideoUpdateResponse.parse_obj(response_json)

    def patch_video_params(self, video_params: VideoParams) -> VideoUpdateResponse:
        """Update video parameters using PATCH method.

        Args:
            video_params: Parameters of video.
        """
        video_params_dict: dict = \
            loads(video_params.json(exclude={'video_id'}, exclude_none=True))
        response_json = self.request(
            method='PATCH',
            path=f'video/{video_params.video_id}',
            json=video_params_dict,
        )
        return VideoUpdateResponse.parse_obj(response_json)

    def delete(self, video_id: str) -> BaseResponse:
        """Delete video.

        Args:
            video_id: The id of video.
        """
        response_json = self.request(
            method='DELETE',
            path=f'video/{video_id}',
        )
        return BaseResponse.parse_obj(response_json)
    pass
