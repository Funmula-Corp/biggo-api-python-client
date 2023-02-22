"""This module defines an enum of limit type"""

from enum import Enum, auto


class Limit(Enum):
    """Type of limit"""
    everyone = 0
    limit_myself = auto()
    non_public = auto()
    pass
