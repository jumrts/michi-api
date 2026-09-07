"""Login use case."""

from src.domain.entities.user import User
from src.domain.exceptions import InvalidCredentialsError
from src.infrastructure.security.jwt import create_access_token
from src.infrastructure.security.password import verify_password


class Login:
    """Login a user."""

    def __init__(self, user_repository):
        """Initialize the service with the repository."""
        self._user_repository = user_repository

    async def execute(self, email: str, password: str) -> tuple[User, str]:
        """Login a user.

        Arguments:
            email: str
                The email of the user.
            password: str
                The password of the user.

        Returns:
            tuple[User, str]
                The user and the token.
        """

        user = await self._user_repository.get_by_email(email)

        if not user:
            raise InvalidCredentialsError("Invalid credentials")

        if not verify_password(password, user.password):
            raise InvalidCredentialsError("Invalid credentials")

        token = create_access_token(user.id)

        return User(
            id=user.id,
            name=user.name,
            email=user.email,
        ), token
