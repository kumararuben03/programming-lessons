<template>
  <v-row>
    <v-col cols="12">
      <v-progress-linear
        :model-value="percentage"
        height="25"
        :color="progressBarColor"
        :background-color="progressBarColor"
        :style="progressBarStyle"
      >
        {{ percentage.toFixed(0) }}%
      </v-progress-linear>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: {
    percentage: {
      type: Number,
      required: true,
    },
  },
  computed: {
    progressBarColor() {
      return this.percentage === 100 ? "success" : "error";
    },
    progressBarStyle() {
      return { "background-size": `${this.percentage}%` };
    },
  },
};
</script>

<style scoped>
.progress-container {
  position: relative;
  overflow: hidden;
}

.progress-container::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: var(--progress-width, 0%);
  background-color: var(--progress-color, var(--v-primary-base));
  transition: width 0.3s ease;
  z-index: 1;
}

.v-progress-linear {
  position: relative;
  z-index: 2;
}
</style>
