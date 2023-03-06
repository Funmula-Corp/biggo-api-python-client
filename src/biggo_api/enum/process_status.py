"""This module defines an enum of process status."""

from enum import Enum


class ProcessStatus(Enum):
    """Types of process status"""
    INQUEUE = 0
    COMPLETE = 13
    pass
