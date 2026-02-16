import type { DecisionResponse } from "../api";

interface Props {
  data: DecisionResponse;
}

const DecisionResult = ({ data }: Props) => {
  return (
    <div style={{ marginTop: "20px", border: "1px solid #ccc", padding: "20px" }}>
      <h3>Decision: {data.decision}</h3>
      <p>Confidence: {data.confidence}</p>
      <p>Risk Score: {data.risk_score}</p>

      <h4>Reasons</h4>
      <ul>
        {data.reasons.map((reason, index) => (
          <li key={index}>{reason}</li>
        ))}
      </ul>

      <h4>Extracted Facts</h4>
      <pre>{JSON.stringify(data.extracted_facts, null, 2)}</pre>

      <h4>Supporting Evidence</h4>
      <ul>
        {data.supporting_evidence.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

      <p>
        <strong>Audit Trace ID:</strong> {data.audit_trace_id}
      </p>
    </div>
  );
};

export default DecisionResult;
