"""Database engine, session factory, and the get_db dependency."""

import asyncio

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.infrastructure.config.settings import database_settings

engine = create_async_engine(database_settings.database_url, echo=True)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def check_connection() -> None:
    """Check the connection to the database on startup."""
    max_retries = 3
    retry_delay = 1

    for attempt in range(max_retries):
        try:
            async with engine.connect():
                logger.info("Conexão com o Postgres OK!")
                return
        except Exception as e:
            if attempt == max_retries - 1:
                logger.error(
                    f"Falha na conexão com Postgres após {max_retries} tentativas: {e}"
                )
                raise
            logger.warning(
                f"Tentativa {attempt + 1} falhou, tentando de novo em {retry_delay}s: {e}"
            )
            await asyncio.sleep(retry_delay)
            retry_delay *= 2


async def get_db() -> AsyncSession:
    async with async_session_factory() as session:
        yield session
