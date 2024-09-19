<template>
  <div class="properties">
    <h1>{{ fullName }}</h1>
    <input v-model="firstName" placeholder="First Name" class="input-field" />
    <input v-model="lastName" placeholder="Last Name" class="input-field" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: "Kumara Ruben",
      lastName: "Kumaravelloo",
    };
  },
  computed: {
    fullName() {
      return `${this.firstName} ${this.lastName}`;
    },
  },
};
</script>
