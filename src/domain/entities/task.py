"""The Task entity."""

from dataclasses import dataclass


@dataclass
class Task:
    """
    A task represents a unit of work that needs to be completed.

    Attributes:
        title: str
            The title of the task.
        due_date: datetime
            The due date of the task.
        completed: bool
            Whether the task is completed or not.
    """

    title: str
    due_date: str
    completed: bool

    def complete(self) -> None:
        """Mark the task as completed."""
        if self.completed:
            raise ValueError("Task is already completed")
        self.completed = True
