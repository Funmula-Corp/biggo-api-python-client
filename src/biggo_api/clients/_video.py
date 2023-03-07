"""The API client of video."""

from json import loads
from os import stat

from biggo_api.clients._base import BaseInstanceClient
from biggo_api.data_models.video import VideoParams
from biggo_api.responses import (
    VideoDeleteResponse,
    VideoPermissionResponse,
    VideoResponse,
    VideoUpdateResponse,
    VideoUploadResponse,
)


class VideoClient(BaseInstanceClient):
    """Client to access video API."""

    def has_permission(self) -> VideoPermissionResponse:
        """Verify permission of client to upload video.

        Examples:
            >>> video_client.has_permission()
            VideoPermissionResponse(result=True, at_userid='BigGoUserID', region='tw', userid='USERID')
        """
        response_json = self.request(
            method='POST',
            path='video_auth/self',
        )
        return VideoPermissionResponse.parse_obj(response_json)

    def upload(self, file: str) -> VideoUploadResponse:
        """Upload video from local file.

        Args:
            file: The file path & name of video file.

        Examples:
            Upload local video file at current working directory.

            >>> video_client.upload(file='./SAMPLE_VIDEO.mp4')
            VideoUploadResponse(result=True, video_id='VIDEO_ID')
        """
        # get file stat
        file_stat = stat(file)
        # get file size
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
        """Get video by its id.

        Args:
            video_id: The id of video.

        Examples:
            >>> video_response = video_client.get(video_id='VIDEO_ID')
            >>> video_response
            VideoResponse(result=True, user=VideoUserInfo(...), video=[BigGoVideo(...)], size=1)
            >>> video_response.video
            BigGoVideo(video_id='VIDEO_ID', ...)
        """
        response_json = self.request(
            method='GET',
            path=f'video/{video_id}',
        )
        return VideoResponse.parse_obj(response_json)

    def update(self, video_params: VideoParams) -> VideoUpdateResponse:
        """Update video parameters using POST method.

        In this method, video_id, access, description and title in VideoParams are required.
        Use `partial_update` method to update partial parameters.

        Args:
            video_params: Parameters of video.

        Examples:
            Initialize VideoParams object then post it.

            >>> video_params = VideoParams(
            ...     video_id='VIDEO_ID',
            ...     access=Access.PRIVATE,
            ...     description='DESCRIPTION',
            ...     title='TITLE',
            ... )
            >>> video_client.update(video_params=video_params)
            VideoUpdateResponse(result=True)
        """
        # convert VideoParams object to dictionary
        video_params_dict: dict = \
            loads(video_params.json(exclude={'video_id'}))
        response_json = self.request(
            method='POST',
            path=f'video/{video_params.video_id}',
            json=video_params_dict,
        )
        return VideoUpdateResponse.parse_obj(response_json)

    def partial_update(self, video_params: VideoParams) -> VideoUpdateResponse:
        """Update video parameters using PATCH method.

        Args:
            video_params: Parameters of video.

        Examples:
            Initialize VideoParams object then patch it.

            >>> video_params = VideoParams(
            ...     video_id='VIDEO_ID',
            ...     access=Access.UNLISTED,
            ... )
            >>> video_client.partial_update(video_params=video_params)
            VideoUpdateResponse(result=True)
        """
        # convert VideoParams object to dictionary
        video_params_dict: dict = \
            loads(video_params.json(exclude={'video_id'}, exclude_none=True))
        response_json = self.request(
            method='PATCH',
            path=f'video/{video_params.video_id}',
            json=video_params_dict,
        )
        return VideoUpdateResponse.parse_obj(response_json)

    def delete(self, video_id: str) -> VideoDeleteResponse:
        """Delete video by its id.

        Args:
            video_id: The id of video.

        Examples:
            >>> video_client.delete(video_id='VIDEO_ID')
            VideoDeleteResponse(result=True)
        """
        response_json = self.request(
            method='DELETE',
            path=f'video/{video_id}',
        )
        return VideoDeleteResponse.parse_obj(response_json)
    pass
