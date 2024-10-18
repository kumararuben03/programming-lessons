<template>
  <h1>Admin</h1>
  <v-btn @click="logout">Logout</v-btn>
</template>

<script setup>
const logout = () => {
  const roleKey = "userRole";
  console.log("Before removal:", localStorage.getItem(roleKey));
  localStorage.removeItem(roleKey);
  console.log("After removal:", localStorage.getItem(roleKey));
  window.location.href = "/roles";
};
</script>
