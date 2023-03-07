"""This module defines an enum of access type"""

from enum import Enum, auto


class Access(Enum):
    """Types of access"""
    PUBLIC = 0
    PRIVATE = auto()
    UNLISTED = auto()
    pass
