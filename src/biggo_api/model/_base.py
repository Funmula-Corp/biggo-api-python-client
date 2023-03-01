"""This module defines the base class of all models"""

from dataclasses import asdict, dataclass, fields


@dataclass
class Base:
    """Base class of all models

    This class can convert data between dict and class with custom aliases and exclude fields

    Attributes:
        _ALIASES: A dict object for aliases mapping. Convert attribute name to server's field name
        _EXCLUDE_FIELDS: A list of attribute name to exclude in function `to_dict`
    """
    _ALIASES = {}
    _EXCLUDE_FIELDS = []

    @classmethod
    def from_dict(cls, dict_data: dict):
        """Declare a class object from dict object

        Args:
            dict_data: The dict object to convert
        """
        reversed_aliases = {v: k for k, v in cls._ALIASES.items()}
        derived_dict = {}
        valid_fields = [field.name for field in fields(cls)]
        for key in dict_data:
            if key in valid_fields:
                derived_dict[key] = dict_data[key]
                pass
            if key in reversed_aliases:
                derived_dict[reversed_aliases[key]] = dict_data[key]
                pass
            pass
        return cls(**derived_dict)

    def to_dict(self, exclude_none: bool = True) -> dict:
        """Convert this class to dict object

        This function convert attribute to its alias and remove key with `None` value

        Args:
            exclude_none: set to False will keep keys with `None` value
        """
        dict_data = asdict(self)
        for ori, alias in self._ALIASES.items():
            dict_data[alias] = dict_data[ori]
            del dict_data[ori]
            pass
        for exclude_field in self._EXCLUDE_FIELDS:
            if exclude_field in dict_data:
                del dict_data[exclude_field]
                pass
            pass
        if exclude_none:
            dict_data = {
                key: value for key, value in dict_data.items()
                if value is not None
            }
            pass
        return dict_data
    pass
