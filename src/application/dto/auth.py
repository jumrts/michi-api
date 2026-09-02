"""Auth dto's"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthOutput:
    """
    The output data returned after a successful authentication.

    Attributes:
        name: str
            The name of user.
        token: str
            The auth token.
    """

    name: str
    token: str
