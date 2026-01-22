from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

@api_router.get("/health", tags=["Health"])
async def api_health():
    return {"status": "ok"}