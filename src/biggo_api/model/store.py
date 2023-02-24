"""The models of user store"""

from dataclasses import dataclass

from biggo_api.model._base import Base


@dataclass
class StoreResponse(Base):
    """This class represents a store"""
    name: str
    nindex: str
    pass
