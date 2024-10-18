<template>
  <div>
    <MyInput
      color="yellow"
      @input="handleInput"
      prependContent="mdi-checkbox-blank-circle"
      appendContent="mdi-checkbox-blank-circle-outline"
    >
    </MyInput>
    <p>{{ inputValue }}</p>
    <Button @click="showMessage"></Button>
  </div>
</template>

<script>
import MyInput from "./../components/MyInput.vue";
import Button from "./../components/Button.vue";

export default {
  data() {
    return {
      inputValue: "",
      showDisplay: false,
    };
  },
  methods: {
    handleInput(event) {
      if (event.target) {
        this.inputValue = event.target.value;
      }
    },

    showMessage(event) {
      if (event.target) {
        this.showDisplay = !this.showDisplay;
      }
    },
  },
};
</script>
