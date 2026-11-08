"""The contract for the Settlement repository."""

from abc import ABC, abstractmethod

from src.domain.entities.settlement import Settlement


class SettlementRepository(ABC):
    """The definition of the contract for the Settlement repository."""

    @abstractmethod
    def create(self, income: Settlement) -> None:
        """Create a new settlement in the database."""

    @abstractmethod
    def get(self) -> list[Settlement]:
        """Get all setlement from the database."""

    @abstractmethod
    def get_by_id(self, income_id: int) -> Settlement:
        """Get an settlement by its ID from the database."""

    @abstractmethod
    def delete(self, income_id: int) -> None:
        """Delete an settlement from the database."""

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> list[Settlement]:
        """Get all settlement for a user by its ID from the database."""
