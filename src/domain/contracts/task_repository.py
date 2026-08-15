"""The contract for the Task repository."""

from abc import ABC, abstractmethod

from src.domain.entities.task import Task


class TaskRepository(ABC):
    """The definition of the contract for the Task repository."""

    @abstractmethod
    def create(self, task: Task) -> None:
        """Create a new task in the database."""

    @abstractmethod
    def get(self) -> list[Task]:
        """Get all tasks from the database."""

    @abstractmethod
    def get_by_id(self, task_id: int) -> Task:
        """Get a task by its ID from the database."""

    @abstractmethod
    def update(self, task: Task) -> None:
        """Update a task in the database."""

    @abstractmethod
    def delete(self, task_id: int) -> None:
        """Delete a task from the database."""
