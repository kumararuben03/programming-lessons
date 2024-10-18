<template>
  <v-row>
    <v-col cols="12">
      <v-text-field
        label="Add a new task"
        v-model="newTask"
        @keyup.enter="handleEnterKey"
      ></v-text-field>
      <v-btn @click="addTask" color="primary">ADD</v-btn>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      newTask: "",
    };
  },
  methods: {
    addTask() {
      if (this.newTask.trim() !== "") {
        this.$emit("add-task", this.newTask);
        this.newTask = "";
      }
    },
    handleEnterKey(event) {
      if (event.keyCode === 13) {
        this.addTask();
      }
    },
  },
};
</script>
