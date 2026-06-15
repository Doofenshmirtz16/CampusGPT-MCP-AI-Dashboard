const API_URL = "http://localhost:8000";

export async function askCampusGPT(
  query: string
) {
  const response = await fetch(
    `${API_URL}/chat?query=${encodeURIComponent(query)}`
  );

  return response.json();
}