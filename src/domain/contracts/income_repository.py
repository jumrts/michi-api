"""The contract for the Income repository."""

from abc import ABC, abstractmethod

from src.domain.entities.income import Income


class IncomeRepository(ABC):
    """The definition of the contract for the Income repository."""

    @abstractmethod
    def create(self, income: Income) -> None:
        """Create a new income in the database."""

    @abstractmethod
    def get(self) -> list[Income]:
        """Get all incomes from the database."""

    @abstractmethod
    def get_by_id(self, income_id: int) -> Income:
        """Get an income by its ID from the database."""

    @abstractmethod
    def delete(self, income_id: int) -> None:
        """Delete an income from the database."""

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> list[Income]:
        """Get all incomes for a user by its ID from the database."""
