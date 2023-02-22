"""The models of user"""

from dataclasses import dataclass
from typing import Optional, Union

from biggo_api.model._base import Base
from biggo_api.model.store import Store


@dataclass
class User(Base):
    """This class represents a user"""
    _ALIASES = {
        'at_user_id': 'at_userid',
        'is_verify_ecomm': 'isVerifyEComm',
        'is_verify_user': 'isVerifyUser',
        'profile_image': 'profileimg',
        'user_id': 'userid',
        'is_my_video': 'is_myvideo',
    }
    at_user_id: str
    description: str
    is_verify_ecomm: bool
    is_verify_user: bool
    name: str
    personal_url: Union[str, list[str]]
    profile_image: list[str]
    user_id: str
    all_like_count: Optional[int] = None
    follow_count: Optional[int] = None
    follower_count: Optional[int] = None
    is_follow: Optional[bool] = None
    is_my_video: Optional[bool] = None
    store_list: Optional[list[Store]] = None
    pass
