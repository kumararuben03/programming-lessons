<template>
  <h1
    :class="{
      active: isActive,
      'text-danger': hasError,
      'text-success': isActive,
    }"
  >
    Dynamic Class Binding
  </h1>
  <button @click="toggleActive">Toggle Active</button>
  <button @click="toggleError">Toggle Error</button>
  <br />
  <div :style="[baseStyle, { color: textColor, fontSize: fontSize + 'px' }]">
    Dynamic Style Binding
  </div>
  <input v-model="textColor" placeholder="Enter text color" />
  <input v-model="fontSize" type="number" placeholder="Enter font size" />
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
      hasError: false,
      textColor: "black",
      fontSize: 16,
      baseStyle: {
        padding: "10px",
        border: "1px solid #ccc",
      },
    };
  },

  methods: {
    toggleActive() {
      this.isActive = !this.isActive;
      console.log(this.isActive);
    },

    toggleError() {
      this.hasError = !this.hasError;
      console.log(this.hasError);
    },
  },
};
</script>

<style>
.text-danger {
  color: red;
}

.text-success {
  color: green;
}
</style>
