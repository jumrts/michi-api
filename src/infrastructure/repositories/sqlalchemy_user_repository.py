"""SQLAlchemy implementation of the User repository."""

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.contracts.user_repository import UserRepository
from src.domain.entities.user import User
from src.domain.exceptions import NotFoundError
from src.infrastructure.database.models.user import UserModel


class SQLAlchemyUserRepository(UserRepository):
    """The SQLAlchemy implementation of the User repository."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user: User) -> User:
        """
        Create a new user.

        Arguments:
            user: User
                The user to create.

        Returns:
            User
                The created user.
        """
        model = UserModel(
            name=user.name,
            email=user.email,
            password=user.password,
        )

        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)

        return User(
            id=model.id,
            email=model.email,
            name=model.name,
        )

    async def get(self) -> list[User]:
        """
        Get all users.

        Returns:
            list[User]
                A list of users.
        """
        return await self.db.execute(UserModel.query.all())

    async def get_by_id(self, user_id: int) -> User:
        """
        Get a user by its ID.

        Arguments:
            user_id: int
                The ID of the user to get.

        Returns:
            User
                The user with the given ID.
        """
        return await self.db.execute(UserModel.query.get(user_id))

    async def get_by_email(self, email: str) -> User:
        """
        Get a user by its email.

        Arguments:
            email: str
                The email of the user to get.

        Returns:
            User
                The user with the given email.
        """
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def update(self, user: User) -> None:
        """
        Update a user.

        Arguments:
            user: User
                The user to update.
        """
        stmt = select(UserModel).where(UserModel.id == user.id)
        result = await self.db.execute(stmt)

        user_model = result.scalar_one_or_none()

        if user_model is None:
            raise NotFoundError("User not found")

        user_model.name = user.name
        user_model.email = user.email
        user_model.password = user.password

        await self.db.commit()
        await self.db.refresh(user_model)

    async def delete(self, user_id: int) -> None:
        """
        Delete a user.

        Arguments:
            user_id: int
                The ID of the user to delete.
        """
        stmt = delete(UserModel).where(UserModel.id == user_id)

        await self.db.execute(stmt)
        await self.db.commit()
