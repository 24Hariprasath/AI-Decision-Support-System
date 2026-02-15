import logging
from app.services.rag_services import retrieve_evidence
from app.services.reasoning_services import evaluate_decision
from app.utils.ids import generate_trace_id
from app.schemas.decisions import DecisionResponse, DecisionRequest

logger = logging.getLogger(__name__)


def process_decision(request: DecisionRequest) -> DecisionResponse:
    logger.info("Starting decision processing")

    # Step 1: Retrieve Evidence
    logger.info("Retrieving supporting evidence")
    evidence = retrieve_evidence(
        question=request.decision_question,
        documents=request.documents
    )

    # Step 2: Evaluate Decision
    logger.info("Evaluating decision logic")
    decision, confidence, reasons, risk_score, extracted_facts = evaluate_decision(evidence)

    # Step 3: Generate Trace ID
    trace_id = generate_trace_id()
    logger.info(f"Decision completed | Trace ID: {trace_id}")

    return DecisionResponse(
        decision=decision,
        confidence=confidence,
        reasons=reasons,
        supporting_evidence=evidence,
        audit_trace_id=trace_id,
        risk_score=risk_score,
        extracted_facts=extracted_facts
    )

