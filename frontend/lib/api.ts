const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function apiFetch<T = any>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const res = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });

  if (!res.ok) {
    let message = "Something went wrong";
    try {
      const errorData = await res.json();
      message = errorData.detail || errorData.message || message;
    } catch {
      message = res.statusText || message;
    }
    throw new Error(message);
  }

  return res.json();
}