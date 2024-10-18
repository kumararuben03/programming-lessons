<template>
  <v-container>
    <v-form @submit.prevent>
      <v-row align="center" justify="center">
        <v-col cols="auto">
          <v-btn @click="onSubmit('admin')">Admin</v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn @click="onSubmit('premiumuser')">Premium User</v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn @click="onSubmit('regularuser')">Regular User</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const onSubmit = (role) => {
  const roleKey = "userRole";
  const validRoles = ["admin", "premiumuser", "regularuser"];

  if (!validRoles.includes(role)) {
    console.error("Invalid role");
    return;
  }

  localStorage.setItem(roleKey, role);

  // Use router to navigate
  router.push("/admin");
};
</script>
