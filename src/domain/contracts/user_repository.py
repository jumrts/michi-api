"""The contract for the User repository."""

from abc import ABC, abstractmethod

from src.domain.entities.user import User


class UserRepository(ABC):
    """The definition of the contract for the User repository."""

    @abstractmethod
    def create(self, user: User) -> None:
        """Create a new user in the database."""

    @abstractmethod
    def get(self) -> list[User]:
        """Get all users from the database."""

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        """Get a user by its ID from the database."""

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        """Get a user by its email from the database."""

    @abstractmethod
    def update(self, user: User) -> None:
        """Update a user in the database."""

    @abstractmethod
    def delete(self, user_id: int) -> None:
        """Delete a user from the database."""
