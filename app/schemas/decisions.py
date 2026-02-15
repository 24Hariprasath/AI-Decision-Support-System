from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class DecisionRequest(BaseModel):
    decision_question: str
    documents: Optional[List[str]] = None


class DecisionResponse(BaseModel):
    decision: str
    confidence: float
    reasons: List[str]
    supporting_evidence: List[str]
    audit_trace_id: str
    risk_score: Optional[int] = None
    extracted_facts: Optional[Dict[str, Any]] = None
