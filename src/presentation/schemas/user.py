"""The schemas user."""

from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    """
    The request schema for creating a new user.

    Attributes:
        name: str
            The name of the user.
        email: EmailStr
            The email of the user.
        password: str
            The password of the user.
    """

    name: str
    email: EmailStr
    password: str
