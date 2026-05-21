"""
Purpose: Initialize FastAPI application with CORS, Sentry, and API router

Structure:
    app (FastAPI): output - Configured FastAPI application instance
    custom_generate_unique_id (func): config - Generate OpenAPI operation IDs from route tag + name

Relationships:
    Consumes: core.config.settings, api.main.api_router
    Produces: FastAPI app (consumed by uvicorn)

Semantics:
    Domain: application
    Logic: [Sentry enabled only in non-local environments, CORS origins from settings]
"""

import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings


def custom_generate_unique_id(route: APIRoute) -> str:
    """Purpose: Generate OpenAPI operation ID as '{tag}-{name}' for client codegen"""
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
