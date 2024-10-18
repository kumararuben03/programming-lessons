<template>
  <div v-if="showBeforeMountMessage">
    beforeMount: Component is about to be mounted. Initializing message...
  </div>

  <div v-if="showMountedMessage">
    mounted: Component is mounted and in the DOM. Message: {{ message }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      showBeforeMountMessage: true,
      showMountedMessage: false,
    };
  },

  beforeMount() {
    this.message = "Hello from beforeMount!";
  },

  mounted() {
    this.showBeforeMountMessage = false;
    this.showMountedMessage = true;
  },
};
</script>
