import DocumentUpload from "./components/DocumentUpload";
import DecisionPanel from "./components/DecisionPanel";

function App() {
  return (
    <div style={{ padding: "40px" }}>
      <h1>AI Decision Support System</h1>
      <DocumentUpload />
      <DecisionPanel />
    </div>
  );
}

export default App;
