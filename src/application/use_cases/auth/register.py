"""The register use case."""

from src.application.dto.auth import AuthOutput
from src.application.use_cases.users.create_user import CreateUser
from src.domain.contracts.user_repository import UserRepository
from src.infrastructure.security.jwt import create_access_token


class Register:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(
        self,
        name: str,
        email: str,
        password: str,
    ) -> AuthOutput:
        user = await CreateUser(user_repository=self._user_repository).execute(
            name=name,
            email=email,
            password=password,
        )

        token = create_access_token(user.id)

        return AuthOutput(
            name=user.name,
            token=token,
        )
