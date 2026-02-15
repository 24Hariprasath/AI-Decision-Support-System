from pydantic import BaseModel
from typing import Optional


class ExtractedFacts(BaseModel):
    credit_score: Optional[int] = None
    annual_income: Optional[float] = None
    debt_ratio: Optional[float] = None
    policy_min_credit_score: Optional[int] = None
