from fastapi import APIRouter
from backend.app.api.v1.endpoints import process

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(process.router)

@api_router.get("/health", tags=["Health"])
async def api_health():
    return {"status": "ok"}