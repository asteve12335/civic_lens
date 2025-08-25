import { useEffect, useState } from "react";

function App() {
  const [apiStatus, setApiStatus] = useState(null);

  useEffect(() => {
    // Call backend (running on port 8000 inside docker-compose)
    fetch("http://localhost:8000/health/")
      .then((res) => res.json())
      .then((data) => setApiStatus(data))
      .catch((err) => console.error("API error:", err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">CivicLens Frontend</h1>
      <p className="mt-4">
        Backend Status:{" "}
        {apiStatus ? (
          <span className="text-green-600">✅ {apiStatus.status}</span>
        ) : (
          <span className="text-red-600">❌ Not Connected</span>
        )}
      </p>
    </div>
  );
}

export default App;
