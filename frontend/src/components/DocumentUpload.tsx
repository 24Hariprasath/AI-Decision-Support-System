import { useState } from "react";
import { uploadDocument } from "../api";

const DocumentUpload = () => {
  const [file, setFile] = useState<File | null>(null);
  const [documentType, setDocumentType] = useState<string>("policy");
  const [message, setMessage] = useState<string>("");

  const handleUpload = async () => {
    if (!file) return;

    try {
      const result = await uploadDocument(file, documentType);
      setMessage(result.message);
    } catch {
      setMessage("Upload failed");
    }
  };

  return (
    <div style={{ marginBottom: "30px" }}>
      <h2>Upload Document</h2>

      <select
        value={documentType}
        onChange={(e) => setDocumentType(e.target.value)}
      >
        <option value="policy">Policy Document</option>
        <option value="applicant">Applicant Document</option>
      </select>

      <input
        type="file"
        onChange={(e) => {
          if (e.target.files) {
            setFile(e.target.files[0]);
          }
        }}
        style={{ marginLeft: "10px" }}
      />

      <button onClick={handleUpload} style={{ marginLeft: "10px" }}>
        Upload
      </button>

      <p>{message}</p>
    </div>
  );
};

export default DocumentUpload;
