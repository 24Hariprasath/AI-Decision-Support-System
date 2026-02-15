from typing import Tuple, List
from app.extraction.fact_extractor import extract_facts


def evaluate_decision(evidence: List[str]) -> Tuple[str, float, List[str], int, Dict]:
    facts = extract_facts(evidence)

    risk_score = 0
    reasons = []

    if facts.credit_score:
        if facts.credit_score < 650:
            risk_score += 50
            reasons.append("Very low credit score.")
        elif facts.credit_score < 700:
            risk_score += 30
            reasons.append("Below preferred credit threshold.")
        else:
            risk_score += 5

    if facts.credit_score and facts.policy_min_credit_score:
        if facts.credit_score < facts.policy_min_credit_score:
            risk_score += 40
            reasons.append("Policy minimum credit score not met.")

    # --- Debt Ratio Risk ---
    if facts.debt_ratio:
        if facts.debt_ratio > 0.5:
            risk_score += 30
            reasons.append("High debt-to-income ratio.")
        elif facts.debt_ratio > 0.4:
            risk_score += 15
            reasons.append("Moderate debt-to-income ratio.")

    # --- Income Stability ---
    if facts.annual_income:
        if facts.annual_income < 40000:
            risk_score += 20
            reasons.append("Low annual income.")
        else:
            risk_score += 5

    # --- Decision Bands ---
    if risk_score >= 70:
        decision = "Reject"
    elif risk_score >= 40:
        decision = "Manual Review"
    else:
        decision = "Approve"

    confidence = min(0.95, 0.5 + (risk_score / 200))

    return decision, round(confidence, 2), reasons, risk_score, facts.dict()


