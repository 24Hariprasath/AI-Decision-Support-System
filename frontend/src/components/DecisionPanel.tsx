import { useState } from "react";
import { makeDecision, type DecisionResponse } from "../api";
import DecisionResult from "./DecisionResult";

const DecisionPanel = () => {
  const [question, setQuestion] = useState<string>("");
  const [result, setResult] = useState<DecisionResponse | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleDecision = async () => {
    try {
      setLoading(true);
      const response = await makeDecision(question);
      setResult(response);
    } catch (error) {
      alert("Decision failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Make Decision</h2>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Enter decision question..."
        style={{ width: "400px" }}
      />

      <button onClick={handleDecision} style={{ marginLeft: "10px" }}>
        {loading ? "Evaluating..." : "Evaluate"}
      </button>

      {result && <DecisionResult data={result} />}
    </div>
  );
};

export default DecisionPanel;
