"""Login use case."""

from src.application.dto.auth import AuthOutput
from src.domain.exceptions import InvalidCredentialsError
from src.infrastructure.security.jwt import create_access_token
from src.infrastructure.security.password import verify_password


class Login:
    """Login a user."""

    def __init__(self, user_repository):
        """Initialize the service with the repository."""
        self._user_repository = user_repository

    async def execute(self, email: str, password: str) -> AuthOutput:
        """Login a user.

        Arguments:
            email: str
                The email of the user.
            password: str
                The password of the user.

        Returns:
            AuthOutput
                The output data returned after a successful authentication.
        """

        user = await self._user_repository.get_by_email(email)

        if not user:
            raise InvalidCredentialsError("Invalid credentials")

        if not verify_password(password, user.password):
            raise InvalidCredentialsError("Invalid credentials")

        token = create_access_token(user.id)

        return AuthOutput(
            name=user.name,
            token=token,
        )
