<template>
  <v-app>
    <v-main>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <v-progress-linear
              :value="percentageCompleted"
              height="25"
              :color="progressBarColor"
              :background-color="progressBarColor"
              :style="progressBarStyle"
              v-model="percentageCompleted"
            >
              {{ percentageCompleted.toFixed(0) }}%
            </v-progress-linear>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <h1 class="text-center">Todo List App</h1>
          </v-col>
        </v-row>
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

        <v-row v-for="(task, index) in tasks" :key="index">
          <v-col cols="12">
            <v-card class="mb-2">
              <div class="list-btns">
                <v-checkbox v-model="task.completed" label="Completed">
                </v-checkbox>
                <div class="edit-btns">
                  <v-btn
                    icon
                    @click="editTask(index)"
                    :disabled="task.editable"
                    color="info"
                  >
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                  <v-btn
                    icon
                    @click="deleteTask(index)"
                    :disabled="task.editable"
                    color="error"
                  >
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </div>
              </div>
              <v-card-text>
                <v-row>
                  <v-col cols="10">
                    <v-text-field
                      v-model="task.text"
                      :disabled="!task.editable"
                      label="Task"
                      dense
                    ></v-text-field>
                  </v-col>
                  <v-col cols="2">
                    <v-btn
                      @click="saveTask(index)"
                      :disabled="!task.editable"
                      color="success"
                      >Save</v-btn
                    >
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      tasks: [],
      newTask: "",
    };
  },

  methods: {
    addTask() {
      if (this.newTask.trim() !== "") {
        this.tasks.push({
          text: this.newTask,
          completed: false,
          editable: false, // Add editable property
        });
        this.newTask = "";
      }
    },

    handleEnterKey(event) {
      if (event.keyCode === 13) {
        this.addTask();
      }
    },

    editTask(index) {
      this.tasks[index].editable = true;
    },

    deleteTask(index) {
      this.tasks.splice(index, 1);
    },

    saveTask(index) {
      this.tasks[index].editable = false;
    },
  },

  computed: {
    percentageCompleted() {
      const totalTasks = this.tasks.length;
      const completedTasks = this.tasks.filter((task) => task.completed).length;
      return totalTasks > 0 ? (completedTasks / totalTasks) * 100 : 0;
    },

    progressBarColor() {
      return this.percentageCompleted === 100 ? "success" : "error";
    },
    progressBarStyle() {
      return { "background-size": `${this.percentageCompleted}%` };
    },
  },
};
</script>

<style>
.v-card-title .v-btn {
  margin-left: 5px;
}

.list-btns {
  display: flex;
  justify-content: space-between;
}

.edit-btns {
  display: flex;
  gap: 10px;
}

.v-progress-linear {
  width: 100%;
  font-weight: bolder;
}

@media only screen and (max-width: 600px) {
  .v-progress-linear {
    margin: 0 auto;
  }
}
</style>
