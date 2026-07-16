// Хранение залогиненного пользователя в localStorage
const USER_STORAGE_KEY = "user";

export function getCurrentUser() {
  const raw = localStorage.getItem(USER_STORAGE_KEY);
  return raw ? JSON.parse(raw) : null;
}

export function saveCurrentUser(user) {
  localStorage.setItem(USER_STORAGE_KEY, JSON.stringify(user));
}

export function clearCurrentUser() {
  localStorage.removeItem(USER_STORAGE_KEY);
}
