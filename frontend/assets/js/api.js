// Обёртка над fetch для запросов к backend (тот же origin, что и frontend)
export async function apiRequest(path, options = {}) {
  const res = await fetch(path, {
    ...options,
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
  });

  if (!res.ok) {
    let detail = `Ошибка запроса (${res.status})`;
    try {
      const data = await res.json();
      if (data.detail) detail = data.detail;
    } catch {
      // тело ответа не JSON — оставляем сообщение по умолчанию
    }
    throw new Error(detail);
  }

  if (res.status === 204) return null;
  return res.json();
}
