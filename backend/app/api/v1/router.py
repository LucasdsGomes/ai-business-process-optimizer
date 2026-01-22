from fastapi import APIRouter
from backend.app.api.v1.processes.router import router as process_router
from backend.app.api.v1.endpoints.health import router as health_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(process_router)
api_router.include_router(health_router)
