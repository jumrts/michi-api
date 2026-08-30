"""Exception handlers that translate domain errors into HTTP responses."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.exceptions import AlreadyExistsError, NotFoundError


def register_exception_handlers(app: FastAPI) -> None:
    """Register all domain exception handlers on the given FastAPI app."""

    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError) -> JSONResponse:
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(AlreadyExistsError)
    async def already_exists_handler(
        request: Request, exc: AlreadyExistsError
    ) -> JSONResponse:
        return JSONResponse(status_code=409, content={"detail": str(exc)})
