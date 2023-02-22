"""This module defind exceptions of BigGo API Client"""


class BigGoAPIException(Exception):
    """Base Exception, all the other exceptions are inherited from it"""

    def __init__(self, code: int, message: str):
        # Call the base class constructor with the parameters it needs
        error_message = f'[{code}] {message}'
        super().__init__(error_message)
        self.code = code
        pass
    pass
