"""This module defines data class of video"""

from dataclasses import dataclass
from typing import Optional

from biggo_api.model._base import Base
from biggo_api.model.product import DraftProduct, Product


@dataclass
class EditedVideo(Base):
    """This class is used for updating video settings """
    _ALIASES = {
        'thumbnail_ts': 'thumbnail-ts',
    }
    _EXCLUDE_FIELDS = ['video_id']
    video_id: str
    description: Optional[str] = None
    limit: Optional[str] = None
    product_list: Optional[list[DraftProduct]] = None
    thumbnail_ts: Optional[int] = None
    pass


@dataclass
class NewVideo(Base):
    """This class is used for setting up newly uploaded video"""
    _ALIASES = {
        'thumbnail_ts': 'thumbnail-ts',
    }
    _EXCLUDE_FIELDS = ['video_id']
    video_id: str
    description: str
    limit: str
    product_list: list[DraftProduct]
    thumbnail_ts: int
    pass


@dataclass
class VideoDownload(Base):
    """This class represents specific format's download path of video"""
    mp4: str
    pass


@dataclass
class VideoMeta(Base):
    """This class represents meta data of video"""
    aspect_ratio: Optional[str]
    cover_image: str
    download: VideoDownload
    iso8601_length: str
    length: float
    thumbnails: list[str]
    pass


@dataclass
class VideoStatus(Base):
    """This class represents status of processing video"""
    process_status: int
    process_status_kw: list[str]
    processing: bool
    pass


@dataclass
class Video(Base):
    """This class represents a video"""
    _ALIASES = {
        'at_user_id': 'at_userid',
        'has_product': 'hasProduct',
        'is_verify_ecomm': 'isVerifyEComm',
        'is_verify_user': 'isVerifyUser',
        'profile_image': 'profileimg',
        'user_id': 'userid',
    }
    created_at: str
    description: str
    has_product: bool
    is_edited: bool
    is_like: bool
    is_myvideo: bool
    limit: int
    meta: VideoMeta
    product_count: int
    status: VideoStatus
    str_datetime: str
    timestamp: int
    url: str
    user_id: str
    video_comment_count: int
    video_id: str
    video_like_count: int
    view_count: int
    at_user_id: Optional[str] = None
    is_follow: Optional[bool] = None
    is_private: Optional[bool] = None
    is_verify_ecomm: Optional[bool] = None
    is_verify_user: Optional[bool] = None
    like_list: Optional[list[str]] = None
    name: Optional[str] = None
    product_list: Optional[list[Product]] = None
    profile_image: Optional[str] = None
    pass


@dataclass
class VideoStatistics(Base):
    """This class represents statistics of video"""
    _ALIASES = {
        'unique_user_count': 'uniq_users',
    }
    average_play_time: float
    full_play_percentage: float
    play_time: float
    unique_user_count: int
    pass


@dataclass
class VideoAnalysis(Base):
    """This class represents analysis of video"""
    _ALIASES = {
        'statistics_last_day': 'last_day',
        'statistics_total': 'total',
    }
    cover_image: str
    createtime: str
    createtime_ts: int
    last_timestamp: str
    last_timestamp_ts: int
    length: float
    share_count: int
    statistics_total: VideoStatistics
    statistics_last_day: VideoStatistics
    video_like_count: int
    video_comment_count: int
    view_count: int
    thumbnails: Optional[list[str]] = None
    updatetime: Optional[str] = None
    updatetime_ts: Optional[int] = None
    pass
