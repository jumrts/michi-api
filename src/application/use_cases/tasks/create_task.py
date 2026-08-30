"""Create task use case."""

from datetime import date

from src.domain.contracts.task_repository import TaskRepository
from src.domain.contracts.user_repository import UserRepository
from src.domain.entities.task import Task
from src.domain.exceptions import NotFoundError


class CreateTask:
    """Create a new task."""

    def __init__(
        self,
        task_repository: TaskRepository,
        user_repository: UserRepository,
    ):
        self.task_repository = task_repository
        self.user_repository = user_repository

    async def execute(
        self,
        title: str,
        due_date: date,
        user_id: int,
    ) -> Task:
        """
        Create a new task.

        Arguments:
            title: str
                The title of the task.
            due_date: date
                The due date of the task.
            user_id: int
                The ID of the user who created the task.

        Returns:
            Task
                The created task.
        """
        user = await self.user_repository.get_by_id(user_id)

        if user is None:
            raise NotFoundError("User not found")

        task = Task(
            title=title,
            due_date=due_date,
            completed=False,
            user_id=user_id,
        )

        return await self.task_repository.save(task)
