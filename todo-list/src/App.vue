<template>
  <v-app>
    <v-main>
      <v-container fluid>
        <ProgressLinear :percentage="percentageCompleted" />
        <v-row>
          <v-col cols="12">
            <h1 class="text-center">Todo List App</h1>
          </v-col>
        </v-row>
        <AddTask @add-task="addTask" />
        <!-- 
        <TaskItem
          v-for="(task, index) in tasks"
          :key="index"
          :task="task"
          @edit="editTask(index)"
          @delete="deleteTask(index)"
          @save="saveTask(index)"
          @update:completed="updateTaskCompletion(index, $event)"
        /> -->
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
import ProgressLinear from "./components/ProgressLinear.vue";
import AddTask from "./components/AddTask.vue";
import TaskItem from "./components/TaskItem.vue";

export default {
  data() {
    return {
      tasks: [],
      newTask: "",
    };
  },

  components: {
    ProgressLinear,
    AddTask,
    TaskItem,
  },

  methods: {
    addTask(newTask) {
      this.tasks.push({
        text: newTask,
        completed: false,
        editable: false,
      });
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
    updateTaskCompletion(index, completed) {
      this.$set(this.tasks[index], "completed", completed);
    },
  },

  computed: {
    percentageCompleted() {
      const totalTasks = this.tasks.length;
      const completedTasks = this.tasks.filter((task) => task.completed).length;
      return totalTasks > 0 ? (completedTasks / totalTasks) * 100 : 0;
    },
  },
};
</script>
