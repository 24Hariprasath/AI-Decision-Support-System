from fastapi import FastAPI
from .api import decision_router
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="AI Decision Support System",
    version="1.0.0",
    description="Evidence-based Decision Recommendation Engine"
)

app.include_router(decision_router, prefix="/api/v1")