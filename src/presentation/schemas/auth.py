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

    
class AuthResponse(BaseModel):
    """
    The response schema for a successful authentication.

    Attributes:
        name: str
            The name of the user.
        token: str
            The token of the user.
    """

    name: str
    token: str
