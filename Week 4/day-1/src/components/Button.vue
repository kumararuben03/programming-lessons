<template>
  <v-btn variant="outlined" class="my-3 mx-15"> Click me </v-btn>
</template>

<script>
export default {
  data() {
    return {
      showDisplay: true,
    };
  },

  methods: {
    toggleDisplay() {
      this.showDisplay = !this.showDisplay;
    },
  },
};
</script>
