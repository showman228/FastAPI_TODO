// Логика страницы входа/регистрации (index.html)
import { getCurrentUser, saveCurrentUser } from "./storage.js";
import { apiRequest } from "./api.js";

function initAuthPage() {
  // Если уже залогинены — сразу на список заметок
  if (getCurrentUser()) {
    window.location.href = "notes.html";
    return;
  }

  const loginForm = document.getElementById("login-form");
  const loginError = document.getElementById("login-error");

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    loginError.textContent = "";

    const email = document.getElementById("login-email").value.trim();
    const password = document.getElementById("login-password").value;

    try {
      const user = await apiRequest("/users/login", {
        method: "POST",
        body: JSON.stringify({ email, password }),
      });
      saveCurrentUser(user);
      window.location.href = "notes.html";
    } catch (err) {
      loginError.textContent = "Неверная почта или пароль";
    }
  });

  const registerForm = document.getElementById("register-form");
  const registerError = document.getElementById("register-error");

  registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    registerError.textContent = "";

    const username = document.getElementById("reg-username").value.trim();
    const firstname = document.getElementById("reg-firstname").value.trim();
    const lastname = document.getElementById("reg-lastname").value.trim();
    const email = document.getElementById("reg-email").value.trim();
    const password = document.getElementById("reg-password").value;

    try {
      const user = await apiRequest("/users", {
        method: "POST",
        body: JSON.stringify({ username, email, firstname, lastname, password }),
      });
      saveCurrentUser(user);
      window.location.href = "notes.html";
    } catch (err) {
      registerError.textContent = err.message;
    }
  });
}

document.addEventListener("DOMContentLoaded", initAuthPage);
