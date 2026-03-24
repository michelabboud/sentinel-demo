from fastapi import APIRouter
from app.endpoints import auth, users, groups, tasks

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(groups.router)
api_router.include_router(tasks.router)
