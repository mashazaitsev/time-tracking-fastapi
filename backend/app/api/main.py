"""
Purpose: Register all API route modules into the main API router

Structure:
    api_router (APIRouter): output - Combined router with all route modules

Relationships:
    Consumes: api.routes.login, api.routes.users, api.routes.utils, api.routes.items, api.routes.projects, api.routes.time_entries, api.routes.private
    Produces: api_router (consumed by app.main)

Note:
    Private routes only registered when ENVIRONMENT=local.
"""

from fastapi import APIRouter

from app.api.routes import items, login, private, projects, time_entries, users, utils, vacation_requests
from app.core.config import settings

#all routers get plugged in as features. 
#(if you wanted to add a new feature like 'Comments', you'd create 
# comments.py in the routes folder, then add one line here:
api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(utils.router)
api_router.include_router(items.router)
api_router.include_router(projects.router)
api_router.include_router(time_entries.router)
api_router.include_router(vacation_requests.router)

#gathers all route files into one package and exports it.


if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)
