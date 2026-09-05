"""Create user use case."""

from src.domain.contracts.user_repository import UserRepository
from src.domain.entities.user import User
from src.domain.exceptions import AlreadyExistsError
from src.infrastructure.security.password import hash_password


class CreateUser:
    """Create a new user."""

    def __init__(self, user_repository: UserRepository):
        """Initialize the service with the repository."""
        self._user_repository = user_repository

    async def execute(self, name: str, email: str, password: str) -> User:
        """
        Create a new user.

        Verify that the user does not already exist.

        Arguments:
            name: str
                The name of the user.
            email: str
                The email of the user.
            password: str
                The password of the user.

        Returns:

        """
        already_exists = await self._user_repository.get_by_email(email)

        if already_exists:
            raise AlreadyExistsError("User already exists")

        user = User(name=name, email=email, password=hash_password(password))

        return await self._user_repository.create(user)
