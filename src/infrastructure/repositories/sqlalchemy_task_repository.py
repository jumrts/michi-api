"""SQLAlchemy implementation of the Task repository."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.contracts.task_repository import TaskRepository
from src.domain.entities.task import Task
from src.infrastructure.database.models.task import TaskModel


class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, task: Task, user_id: str) -> Task:
        """
        Create a new task.

        Arguments:
            task: Task
                The task to create.
            user_id: str
                The ID of the user who created the task.

        Returns:
            Task
                The created task.
        """
        model = TaskModel(
            user_id=user_id,
            title=task.title,
            completed=task.completed,
            due_date=task.due_date,
        )

        self.db.add(model)
        await self.db.commit()
        await self.db.refresh(model)  

        return Task(title=model.title, completed=model.completed, due_date=model.due_date)