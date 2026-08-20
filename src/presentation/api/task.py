"""Routes for the Task entity."""

from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.use_cases.tasks.create_task import CreateTask
from src.infrastructure.database.session import get_db
from src.infrastructure.repositories.sqlalchemy_task_repository import (
    SQLAlchemyTaskRepository,
)
from src.infrastructure.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from src.presentation.api.task import Task

router = APIRouter(prefix="/tasks")


@router.post("/create", response_model=Task)
async def create_task(
    title: str,
    user_id: str,
    due_date: str,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Task:
    """
    Create a new task.

    Arguments:
        title: str
            The title of the task.
        due_date: str
            The due date of the task.
        user_id: str
            The ID of the user who created the task.

    Returns:
        Task
            The created task.
    """
    use_case = CreateTask(
        task_repository=SQLAlchemyTaskRepository(db),
        user_repository=SQLAlchemyUserRepository(db),
    )

    return await use_case.execute(title=title, due_date=due_date, user_id=user_id)
