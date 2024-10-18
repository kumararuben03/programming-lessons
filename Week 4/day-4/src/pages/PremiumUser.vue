<template>
  <h1>Premium User</h1>
  <v-btn @click="logout">Logout</v-btn>
</template>

<script>
export default {
  methods: {
    logout() {
      localStorage.removeItem("authToken");
      window.location.href = "/roles";
    },
  },
};
</script>
