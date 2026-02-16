from typing import List, Tuple
from app.llm.llm_client import call_llm
from app.llm.prompts import SYSTEM_PROMPT


def evaluate_decision(evidence: List[str]) -> Tuple[str, float, List[str], int, dict]:
    combined_evidence = "\n\n".join(evidence)

    user_prompt = f"""
    Evidence:
    {combined_evidence}

    Make decision based strictly on evidence.
    """

    result = call_llm(SYSTEM_PROMPT, user_prompt)

    if "error" in result:
        return "Manual Review", 0.5, ["LLM parsing error"], 50, {}

    return (
        result.get("decision", "Manual Review"),
        result.get("confidence", 0.5),
        result.get("reasons", []),
        result.get("risk_score", 50),
        result.get("extracted_facts", {}),
    )
