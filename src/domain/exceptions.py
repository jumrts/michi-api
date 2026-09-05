"""Exceptions for the application."""


class NotFoundError(Exception):
    """Raised when an entity is not found."""


class AlreadyExistsError(Exception):
    """Raised when trying to create an entity that already exists."""


class InvalidCredentialsError(Exception):
    """Raised when the credentials are invalid."""
