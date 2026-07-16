export function formatNoteDate(isoString) {
  const date = new Date(isoString);
  return date.toLocaleString("ru-RU", {
    day: "numeric",
    month: "long",
    hour: "2-digit",
    minute: "2-digit",
  });
}
