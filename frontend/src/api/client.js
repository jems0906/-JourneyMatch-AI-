const API = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

export async function createSession() {
  const response = await fetch(`${API}/sessions`, { method: "POST" });
  return response.json();
}

export async function deleteSession(sessionId) {
  await fetch(`${API}/sessions/${sessionId}`, { method: "DELETE" });
}

export async function getRecommendations(sessionId, prompt) {
  const response = await fetch(`${API}/recommend`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, prompt }),
  });
  return response.json();
}

export async function submitFeedback(sessionId, rating) {
  await fetch(`${API}/feedback`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, rating }),
  });
}

export async function getQualityDashboard() {
  const response = await fetch(`${API}/dashboards/quality`);
  return response.json();
}
