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


class UserResponse(BaseModel):
    """
    The response schema for a user.

    Attributes:
        id: str
            The id of user.
        name: str
            The name of user.
        email: str
            The email of user.
    """

    id: str
    name: str
    email: str
