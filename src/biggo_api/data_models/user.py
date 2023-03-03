"""This module defines data classes of user"""

from typing import Union

from pydantic import BaseModel, Field


class VideoUserInfo(BaseModel):
    all_like_count: int
    at_userid: str
    description: str
    follow_count: int
    follower_count: int
    is_verify_ecomm: bool = Field(alias='isVerifyEComm')
    is_verify_user: bool = Field(alias='isVerifyUser')
    is_follow: bool
    is_myvideo: bool
    name: str
    personal_url: Union[str, list[str]]
    profileimg: str
    userid: str
    pass
