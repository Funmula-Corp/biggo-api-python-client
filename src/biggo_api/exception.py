"""This module defind error of BigGo API."""

from biggo_api.responses import ErrorResponse


class BigGoAPIError(Exception):
    """BigGo API Error object for all 4xx responses with error in response body.

    Attributes:
        response: The error response.
    """
    response: ErrorResponse

    def __init__(self, response: ErrorResponse):
        self.response = response
        super().__init__(self.response)
        pass
    pass
