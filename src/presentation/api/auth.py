"""Routes for the User entity."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.use_cases.users.create_user import CreateUser
from src.infrastructure.config.settings import rate_limit_settings
from src.infrastructure.database.session import get_db
from src.infrastructure.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from src.infrastructure.security.rate_limit import limiter
from src.presentation.schemas.user import CreateUserRequest, UserResponse

router = APIRouter(prefix="/auth")


@router.post("/singup", response_model=UserResponse)
@limiter.limit(rate_limit_settings.auth_limit)
async def create_user(
    request: Request,
    data: CreateUserRequest,
    db: Annotated[AsyncSession, Depends(get_db)],
) -> UserResponse:
    """
    Create a new user.

    Arguments:
        name: str
            The name of the user.
        email: str
            The email of the user.
        password: str
            The password of the user.

    Returns:
        User
            The created user.
    """
    return await CreateUser(user_repository=SQLAlchemyUserRepository(db)).execute(
        name=data.name, email=data.email, password=data.password
    )
