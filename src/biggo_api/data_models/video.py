"""This module defines data classes of video."""

from typing import Any, Optional, Union

from pydantic import BaseModel, Field, conlist

from biggo_api.data_models.product import VideoProducts
from biggo_api.enum.access import Access
from biggo_api.enum.process_status import ProcessStatus


class VideoParams(BaseModel):
    """This class is used for post/patch video settings.
    
    Attributes:
        access: Accessibility of video.
        description: Description of video.
        title: Title of video.
        video_id: Id of video.
    """
    access: Optional[Access] = None
    description: Optional[str] = None
    product_list: Optional[list] = None
    thumbnail_time: Optional[int] = Field(alias='thumbnail-ts')
    title: Optional[str] = None
    video_id: str

    class Config:
        allow_population_by_field_name = True
        pass
    pass


class BigGoVideoMetaDownload(BaseModel):
    """This class represents download path in specific format for the video."""
    mp4: str
    pass


class BigGoVideoMeta(BaseModel):
    """This class represents meta data of video."""
    aspect_ratio: Optional[str]
    cover_image: str
    download: Union[conlist(Any, max_items=0), BigGoVideoMetaDownload]
    iso8601_length: str
    length: float
    thumbnails: list[str]
    pass


class BigGoVideoProcessStatus(BaseModel):
    """This class represents status of processing video."""
    process_status: ProcessStatus
    process_status_kw: list[str]
    processing: bool
    pass


class BigGoVideo(BaseModel):
    """This class represents a video."""
    access: Access
    at_userid: str
    created_at: str
    description: Optional[str]
    has_product: bool = Field(alias='hasProduct')
    is_edited: bool
    is_like: bool
    is_myvideo: bool
    is_follow: bool
    is_verify_ecomm: bool = Field(alias='isVerifyEComm')
    is_verify_user: bool = Field(alias='isVerifyUser')
    limit: Access
    name: str
    product_count: int
    profile_image: str = Field(alias='profileimg')
    status: BigGoVideoProcessStatus
    str_datetime: Optional[str]
    timestamp: int
    url: str
    userid: str
    video_comment_count: int
    video_id: str
    video_like_count: int
    view_count: int
    is_private: Optional[bool] = None
    like_list: Optional[list[str]] = None
    meta: Optional[BigGoVideoMeta] = None
    product_list: Optional[VideoProducts] = None
    pass
