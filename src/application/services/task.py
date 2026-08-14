"""The service for the Task entity."""

from src.domain.contracts.task_repository import TaskDatabase
from src.domain.entities.task import Task


class TaskService:
    """The service for the Task entity."""

    def __init__(self, task_repository: TaskDatabase):
        """Initialize the service with the repository."""
        self.db = task_repository

    async def create(self, title: str, due_date: str, user_id: int) -> Task:
        """Create a new task."""
        task = Task(title, due_date, False)
        return await self.db.save(task, user_id)