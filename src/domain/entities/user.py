"""The User entity."""

from dataclasses import dataclass


@dataclass
class User:
    """
    A user represents an individual who can create and manage tasks.

    Attributes:
        name: str
            The name of the user.
        email: str
            The email of the user.
        password: str | None
            The password of the user.
        id: int | None
            The ID of the user.
    """

    name: str
    email: str | None = None
    password: str | None = None
    id: int | None = None
