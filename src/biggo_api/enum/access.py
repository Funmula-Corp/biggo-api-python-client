"""This module defines an enum of access type"""

from enum import Enum, auto


class Access(Enum):
    """Type of access"""
    PUBLIC = 0
    PRIVATE = auto()
    UNLISTED = auto()
    pass
