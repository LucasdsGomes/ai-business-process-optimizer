from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.v1.router import api_router

app = FastAPI(
    title="AI Business Process Optimizer",
    version="1.0.0"
)

# ⚠️ ajuste conforme ambiente
origins = [
    "http://localhost:8501",  # Streamlit
    "http://localhost:3000",  # Next.js (se usar no futuro)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

# USO DE HEALTH CHECKS NO PROJETO

# main.py	- App está no ar
# router.py	- API versionada está acessível
# endpoints/health.py -	Saúde detalhada de dependências