// Логика страницы списка заметок (notes.html)
import { getCurrentUser, clearCurrentUser } from "./storage.js";
import { apiRequest } from "./api.js";
import { formatNoteDate } from "./format.js";

function renderNote(task) {
  const li = document.createElement("li");
  li.className = "note-row";

  const a = document.createElement("a");
  a.className = "note-link";
  a.href = `note.html?id=${task.id}`;

  const topLine = document.createElement("div");
  topLine.className = "note-top-line";

  const title = document.createElement("span");
  title.className = "note-title";
  title.textContent = task.name;

  const date = document.createElement("span");
  date.className = "note-date";
  date.textContent = formatNoteDate(task.created_at);

  topLine.append(title, date);

  const preview = document.createElement("p");
  preview.className = "note-preview";
  preview.textContent = task.description || "";

  a.append(topLine, preview);
  li.append(a);
  return li;
}

async function initNotesPage() {
  const user = getCurrentUser();
  if (!user) {
    window.location.href = "index.html";
    return;
  }

  document.getElementById("account-avatar").textContent = user.username.slice(0, 2).toUpperCase();
  document.getElementById("account-username").textContent = user.username;
  document.getElementById("account-email").textContent = user.email;

  document.getElementById("logout-btn").addEventListener("click", () => {
    clearCurrentUser();
    window.location.href = "index.html";
  });

  document.getElementById("compose-btn").addEventListener("click", () => {
    window.location.href = "note.html";
  });

  const notesList = document.querySelector(".notes-list");

  try {
    const tasks = await apiRequest(`/tasks/user/${user.id}`);

    notesList.innerHTML = "";
    if (tasks.length === 0) {
      const empty = document.createElement("div");
      empty.className = "list-empty";
      empty.innerHTML = `
        <div class="list-empty-title">Пока нет заметок</div>
        <div class="list-empty-text">Нажмите «+», чтобы создать первую</div>
      `;
      notesList.replaceWith(empty);
      return;
    }

    tasks.forEach((task) => notesList.appendChild(renderNote(task)));
  } catch (err) {
    notesList.innerHTML = `<div class="list-empty"><div class="list-empty-title">Не удалось загрузить заметки</div></div>`;
  }
}

document.addEventListener("DOMContentLoaded", initNotesPage);
