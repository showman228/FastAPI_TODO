// Логика страницы отдельной заметки (note.html)
import { getCurrentUser } from "./storage.js";
import { apiRequest } from "./api.js";
import { formatNoteDate } from "./format.js";

async function initNotePage() {
  const user = getCurrentUser();
  if (!user) {
    window.location.href = "index.html";
    return;
  }

  const heading = document.getElementById("note-heading");
  const body = document.getElementById("note-body");
  const meta = document.getElementById("note-meta");
  const deleteBtn = document.getElementById("delete-note-btn");

  let taskId = new URLSearchParams(window.location.search).get("id");

  if (taskId) {
    try {
      const task = await apiRequest(`/tasks/${taskId}`);
      heading.textContent = task.name;
      body.textContent = task.description || "";
      meta.textContent = formatNoteDate(task.created_at);
    } catch (err) {
      window.location.href = "notes.html";
      return;
    }
  }

  async function saveNote() {
    const name = heading.textContent.trim();
    const description = body.textContent.trim();
    if (!name) return;

    const payload = { name, description, user_id: user.id };

    if (taskId) {
      await apiRequest(`/tasks/${taskId}`, {
        method: "PUT",
        body: JSON.stringify(payload),
      });
    } else {
      const task = await apiRequest("/tasks", {
        method: "POST",
        body: JSON.stringify(payload),
      });
      taskId = task.id;
      history.replaceState(null, "", `note.html?id=${task.id}`);
      meta.textContent = formatNoteDate(task.created_at);
    }
  }

  heading.addEventListener("blur", saveNote);
  body.addEventListener("blur", saveNote);

  deleteBtn.addEventListener("click", async () => {
    if (!taskId) {
      window.location.href = "notes.html";
      return;
    }
    if (!confirm("Удалить заметку?")) return;
    await apiRequest(`/tasks/${taskId}`, { method: "DELETE" });
    window.location.href = "notes.html";
  });
}

document.addEventListener("DOMContentLoaded", initNotePage);
