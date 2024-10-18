import { computed } from "vue";

export function useDateFormatter() {
  const formatDateToReadable = (dateValue) => {
    if (!dateValue) return "";
    const date = new Date(dateValue);
    const day = String(date.getDate()).padStart(2, "0");
    const month = date.toLocaleDateString("default", { month: "short" });
    const year = date.getFullYear();
    return `${day}-${month}-${year}`;
  };

  const formatDate = (dateValue) => {
    if (!dateValue) return "";
    let date = new Date(dateValue);
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    const year = date.getFullYear();
    return `${year}-${month}-${day}`;
  };

  const maxDate = computed(() => {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    return yesterday;
  });

  return {
    formatDateToReadable,
    formatDate,
    maxDate,
  };
}
