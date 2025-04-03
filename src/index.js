import React, { useState } from "react";

const App = () => {
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState("");

  const handleAnalyze = async () => {
    setLoading(true);
    setResponse("");
    
    try {
      const res = await fetch("http://localhost:5000/analyze_termsheet", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!res.ok) {
        throw new Error(`Server Error: ${res.status} ${res.statusText}`);
      }

      const data = await res.json();
      setResponse(JSON.stringify(data, null, 2));
    } catch (error) {
      setResponse(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>📜 Term Sheet Validator</h1>
      <button
        onClick={handleAnalyze}
        disabled={loading}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          cursor: "pointer",
          backgroundColor: loading ? "#ccc" : "#007bff",
          color: "#fff",
          border: "none",
          borderRadius: "5px",
          marginBottom: "20px",
        }}
      >
        {loading ? "Processing..." : "Analyze Term Sheet"}
      </button>
      <pre
        style={{
          marginTop: "20px",
          textAlign: "left",
          backgroundColor: "#f4f4f4",
          padding: "10px",
          borderRadius: "5px",
          whiteSpace: "pre-wrap",
          wordWrap: "break-word",
        }}
      >
        {response || "Click the button to analyze the term sheet."}
      </pre>
    </div>
  );
};

export default App;
