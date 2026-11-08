"""The contract for the Debtor repository."""

from abc import ABC, abstractmethod

from src.domain.entities.settlement import Settlement
from src.domain.entities.task import Task


class DebtorRepository(ABC):
    """The definition of the contract for the Debtor repository."""

    @abstractmethod
    def create(self, debtor: Task) -> None:
        """Create a new debtor in the database."""

    @abstractmethod
    def get(self) -> list[Task]:
        """Get all debtors from the database."""

    @abstractmethod
    def get_by_id(self, debtor_id: int) -> Task:
        """Get a debtor by its ID from the database."""

    @abstractmethod
    def delete(self, debtor_id: int) -> None:
        """Delete a debtor from the database."""

    @abstractmethod
    def get_settlemens_by_debtor_id(self, debtor_id: int) -> list[Settlement]:
        """Get all settlements for a debtor by its ID from the database."""
