from __future__ import annotations


class AptError(Exception):
    exit_code = 1


class ConfigError(AptError):
    exit_code = 2


class AuthError(AptError):
    exit_code = 3


class NotFoundError(AptError):
    exit_code = 4


class ApiError(AptError):
    """Non-2xx response from a service."""

    exit_code = 5

    def __init__(self, status: int, message: str, body: object = None) -> None:
        super().__init__(f"{status}: {message}")
        self.status = status
        self.body = body
