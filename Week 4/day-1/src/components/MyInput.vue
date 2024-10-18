<template>
  <div class="input-wrapper">
    <v-icon v-if="prependContent">{{ prependContent }}</v-icon>
    <input
      type="text"
      v-model="inputValue"
      :style="{ color: color, backgroundColor: backgroundColor }"
      @input="emitInput"
    />
    <v-icon v-if="appendContent">{{ appendContent }}</v-icon>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputValue: "",
    };
  },

  props: {
    color: {
      type: String,
      default: "white",
    },

    prependContent: {
      type: String,
      default: "mdi mdi-account",
    },

    appendContent: {
      type: String,
      default: "mdi mdi-account-circle",
    },

    backgroundColor: {
      type: String,
      default: "blue",
    },
  },

  methods: {
    emitInput() {
      this.$emit("input", event.target.value);
    },
  },
};
</script>
