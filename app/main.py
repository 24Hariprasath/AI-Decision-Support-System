from fastapi import FastAPI
from .api import decision_router
from app.core.logging import setup_logging
from app.api.v1.documents import router as document_router
from fastapi.middleware.cors import CORSMiddleware

setup_logging()

app = FastAPI(
    title="AI Decision Support System",
    version="1.0.0",
    description="Evidence-based Decision Recommendation Engine"
)

app.include_router(decision_router, prefix="/api/v1")
app.include_router(document_router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
