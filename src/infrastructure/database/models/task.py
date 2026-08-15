"""The Task model."""

import uuid
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.base import Base


class TaskModel(Base):
    """
    The Task model.

    Attributes:
        id: Mapped[uuid.UUID]
            The ID of the task.
        user_id: Mapped[uuid.UUID]
            The ID of the user who created the task.
        title: Mapped[str]
            The title of the task.
        completed: Mapped[bool]
            Whether the task is completed or not.
        due_date: Mapped[datetime | None]
            The due date of the task.
    """

    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    # user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    due_date: Mapped[datetime | None]
