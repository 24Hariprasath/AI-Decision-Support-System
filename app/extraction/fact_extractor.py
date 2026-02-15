import re
from typing import List
from app.extraction.schemas import ExtractedFacts


def extract_facts(evidence: List[str]) -> ExtractedFacts:
    combined_text = " ".join(evidence).lower()

    facts = ExtractedFacts()

    # Extract credit score
    credit_match = re.search(r"credit score (is|of)?\s*(\d{3})", combined_text)
    if credit_match:
        facts.credit_score = int(credit_match.group(2))

    # Extract annual income
    income_match = re.search(r"\$?(\d{2,6})\s*(annually|per year)", combined_text)
    if income_match:
        facts.annual_income = float(income_match.group(1))
    
    # Extract debt ratio (example: debt ratio is 0.45)
    debt_match = re.search(r"debt ratio (is)?\s*(\d\.\d+)", combined_text)
    if debt_match:
        facts.debt_ratio = float(debt_match.group(2))
        
    # Extract policy minimum credit score
    policy_match = re.search(r"credit score (above|greater than)\s*(\d{3})", combined_text)
    if policy_match:
        facts.policy_min_credit_score = int(policy_match.group(2))

    return facts
