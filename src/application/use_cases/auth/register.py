"""The register use case."""

from src.application.use_cases.users.create_user import CreateUser
from src.domain.contracts.user_repository import UserRepository
from src.domain.entities.user import User


class Register:
    def __init__(self, user_repository: UserRepository):
        """Initialize the service with the repository."""
        self._user_repository = user_repository

    async def execute(
        self,
        name: str,
        email: str,
        password: str,
    ) -> User:
        """
        Register a new user.

        Arguments:
            name: str
                The name of the user.
            email: str
                The email of the user.
            password: str
                The password of the user.

        Returns:
            User
                The user that was created.
        """
        user = await CreateUser(user_repository=self._user_repository).execute(
            name=name,
            email=email,
            password=password,
        )

        return User(
            id=str(user.id),
            name=user.name,
            email=user.email,
        )
