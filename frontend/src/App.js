import React, { useState, useEffect } from "react";

function App() {
    const [trafficStatus, setTrafficStatus] = useState("Loading...");

    const startAnalysis = async () => {
        const response = await fetch("http://127.0.0.1:5000/start", {
            method: "POST",
        });
        const data = await response.json();
        setTrafficStatus(data.status);
    };

    return (
        <div>
            <h1>🚦 Smart Traffic Management</h1>
            <button onClick={startAnalysis}>Start Traffic Analysis</button>
            <h3>Status: {trafficStatus}</h3>
        </div>
    );
}

export default App;
