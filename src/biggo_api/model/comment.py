"""The models of video comment"""

from dataclasses import dataclass
from typing import Optional

from biggo_api.model._base import Base


@dataclass
class Comment(Base):
    """This class represents a comment"""
    _ALIASES = {
        'at_user_id': 'at_userid',
        'has_more_comments': 'more_comments',
        'is_verify_ecomm': 'isVerifyEComm',
        'is_verify_user': 'isVerifyUser',
        'parent_user_id': 'parent_userid',
        'type_': 'type',
        'user_id': 'userid',
    }
    # required: commentFormat
    child_comment_count: int
    comment: str
    comment_id: str
    createtime: str
    createtime_timestamp: int
    genelogy: list[str]
    is_liked: bool
    level_count: int
    like_count: int
    has_more_comments: bool
    parent_id: str
    parent_user_id: str
    type_: str
    user_id: str
    video_id: str
    # optional: commentFormat
    has_owner_comment: Optional[bool] = None
    is_owner: Optional[bool] = None
    # optional: union
    at_user_id: Optional[str] = None
    can_delete: Optional[bool] = None
    can_report: Optional[bool] = None
    is_verify_ecomm: Optional[bool] = None
    is_verify_user: Optional[bool] = None
    name: Optional[str] = None
    user_profile: Optional[str] = None
    # optional: createComment
    is_delete: Optional[bool] = None
    # optional: getComments
    child_comments: Optional[list["Comment"]] = None
    pass


@dataclass
class CommentLog(Base):
    """This class represents a comment log"""
    _ALIASES = {
        'comment_owner_id': 'comment_owner_userid',
        'comment_to_user_id': 'comment_to_userid',
        'comment_to_user_name': 'comment_to_name',
    }
    content: str
    comment_owner_id: str
    comment_to_user_id: str
    date: str
    is_owner: bool
    time: str
    video_id: str
    comment_owner_name: Optional[str] = None
    comment_to_user_name: Optional[str] = None
    pass


@dataclass
class NewComment(Base):
    """
    This class is used for creating new comment.

    Attributes:
        video_id: The id of video
        parent_id: The id of parent, could be video id or comment id
        content: The content of comment
        type: comment type, default is text
    """
    _ALIASES = {
        'type_': 'type',
    }
    content: str
    parent_id: str
    video_id: str
    type_: str = 'text'
    pass


@dataclass
class EditedComment(Base):
    """
    This class is used for updating comment

    Attributes:
        comment_id: The id of comment
        content: New content of comment
        type_: The type of comment
    """
    _ALIASES = {
        'type_': 'type',
    }
    _EXCLUDE_FIELDS = ['id']
    comment_id: str
    content: str
    type_: str = 'text'
    pass
