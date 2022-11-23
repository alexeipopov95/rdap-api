"""
Module where all the common exceptions should be.
"""

class BaseErrorException(Exception):
    """ Base exceptions for any kind of errors """
    message = None
    tip = None

    def __init__(self, message, *args: object) -> None:
        super().__init__(message, *args)


class UnhandledErrorException(BaseErrorException):
    """ Base exception for unhandled errors """
    message = (
        "Unhandled exception raised."
        "Please contact for support."
    )


class BaseRequestException(BaseErrorException):
    """ Base exception for requests """
    message = (
        "Something unexpected happend during the requests."
        "Please try again latter."
    )


class ClientHttpException(BaseRequestException):
    """"""


class ClientConnectionError(BaseRequestException):
    """"""


class ClientTimeoutException(BaseRequestException):
    """"""


class ClientRequestException(BaseRequestException):
    """"""