"""The main entry point for the API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.config.settings import app_settings

app = FastAPI(
    title=app_settings.name,
    version=app_settings.version,
    description=app_settings.description,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.origins,
    allow_credentials=app_settings.allow_credentials,
    allow_methods=app_settings.methods,
    allow_headers=app_settings.headers,
)
