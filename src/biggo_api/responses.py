"""This module defines format of response bodies"""

from typing import Any
from pydantic import BaseModel, conlist

from biggo_api.data_models.user import VideoUserInfo
from biggo_api.data_models.video import BigGoVideo


class BaseResponse(BaseModel):
    """Base format of response"""
    result: bool
    pass


class Error(BaseModel):
    """Detailed error code and reason"""
    code: int
    message: str
    pass


class ErrorResponse(BaseResponse):
    """Response of api error"""
    error: Error
    pass


class VideoUploadResponse(BaseResponse):
    """Response of upload video"""
    video_id: str
    pass


class VideoResponse(BaseResponse):
    """Response of get video"""
    user: VideoUserInfo
    video: list[BigGoVideo]
    size: int
    pass


class VideoUpdateResponse(BaseResponse):
    """Response of post/patch video params"""
    data: list = conlist(Any, max_items=0)
    pass


class VideoPermissionResponse(BaseResponse):
    """Response of get video permission"""
    at_userid: str
    region: str
    userid: str
    pass


class UserVideo(BaseModel):
    """Use video dataset"""
    data: list[BigGoVideo]
    size: int
    pass


class UserVideoResponse(BaseResponse):
    """Response of get user's videos"""
    user_video: UserVideo
    pass


class UserLikeVideoResponse(BaseResponse):
    """Response of get user's like videos"""
    like_video: UserVideo
    pass
