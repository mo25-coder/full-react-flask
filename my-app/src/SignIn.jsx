import { useState } from "react";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!username || !password) {
      setMessage("Please fill out all fields.");
      return;
    }

    try {
        const response = await fetch("http://localhost:5000/signin", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
            credentials: "include"  // Ensures the session is sent with the request
          });
          
      

      const data = await response.json();
          console.log("Response data:", data); // Log the response data for debugging
      if (response.ok) {
        setMessage(data.message);
      } else {
        setMessage(data.error);
      }
    } catch (err) {
        console.error("Login failed:", err);
        setMessage("Network error.");
      }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "400px", margin: "auto" }}>
      <h2>Sign In</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          style={{ display: "block", width: "100%", marginBottom: "1rem" }}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          style={{ display: "block", width: "100%", marginBottom: "1rem" }}
        />
        <button type="submit" style={{ padding: "0.5rem 1rem" }}>
          Login
        </button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
