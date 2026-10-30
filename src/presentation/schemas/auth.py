"""The schemas auth."""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    """
    The request schema for logging in a user.

    Attributes:
        email: str
            The email of the user.
        password: str
            The password of the user.
    """

    email: str
    password: str
