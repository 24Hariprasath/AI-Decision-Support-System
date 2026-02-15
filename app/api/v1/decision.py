from fastapi import APIRouter
from app.schemas.decisions import DecisionRequest, DecisionResponse
from app.services.decision_services import process_decision

router = APIRouter()


@router.post("/decision", response_model=DecisionResponse)
def make_decision(request: DecisionRequest):
    """
    Entry point for decision evaluation.
    """
    return process_decision(request)
