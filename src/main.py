"""The main entry point for the API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware

from src.infrastructure.config.settings import app_settings
from src.infrastructure.security.rate_limit import limiter
from src.presentation.api.auth import router as auth_router

app = FastAPI(
    title=app_settings.name,
    version=app_settings.version,
    description=app_settings.description,
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.origins,
    allow_credentials=app_settings.allow_credentials,
    allow_methods=app_settings.methods,
    allow_headers=app_settings.headers,
)

app.include_router(auth_router)
