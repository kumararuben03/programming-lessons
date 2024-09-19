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

<script src="./assets/scripts.js"></script>

<style src="./assets/styles.css"></style>
