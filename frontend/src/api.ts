const BASE_URL = "http://127.0.0.1:8000/api/v1";

export interface DecisionResponse {
  decision: string;
  confidence: number;
  risk_score: number;
  reasons: string[];
  extracted_facts: Record<string, any>;
  supporting_evidence: string[];
  audit_trace_id: string;
}

export async function uploadDocument(
  file: File,
  documentType: string
): Promise<{ message: string }> {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("document_type", documentType);

  const response = await fetch(`${BASE_URL}/documents/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Upload failed");
  }

  return response.json();
}
export async function makeDecision(
  question: string
): Promise<DecisionResponse> {
  const response = await fetch(`${BASE_URL}/decision`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      decision_question: question,
    }),
  });

  if (!response.ok) {
    throw new Error("Decision request failed");
  }

  return response.json();
}


