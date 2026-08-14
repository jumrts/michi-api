"""Routes for the Task entity."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.services.task import TaskService
from src.infrastructure.database.session import get_db
from src.infrastructure.repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository
from src.presentation.api.task import Task

router = APIRouter(prefix="/tasks")


@router.post("/task/create", response_model=Task)
async def create_task(
    title: str, 
    user_id: str, 
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new task.

    Arguments:
        title: str
            The title of the task.
        user_id: str
            The ID of the user who created the task.

    Returns:
        Task
            The created task.
    """
    repository = SQLAlchemyTaskRepository(db)
    service = TaskService(repository)

    task = await service.create(title=title, user_id=user_id)
    return task