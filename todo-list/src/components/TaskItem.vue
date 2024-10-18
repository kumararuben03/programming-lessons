<template>
  <v-row>
    <v-col cols="12">
      <v-card class="mb-2">
        <div class="list-btns">
          <v-checkbox
            :v-model="task.completed"
            label="Completed"
            @change="updateCompleted"
            color="green"
          ></v-checkbox>
          <div class="edit-btns">
            <v-btn
              icon
              @click="$emit('edit')"
              :disabled="task.editable"
              color="info"
            >
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              icon
              @click="$emit('delete')"
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
                @click="$emit('save')"
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
</template>

<script>
export default {
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  //   data() {
  //     return {
  //       localCompleted: this.task.completed,
  //     };
  //   },
  //   watch: {
  //     "task.completed"(newValue) {
  //       this.localCompleted = newValue;
  //     },
  //   },

  methods: {
    updateCompleted(value) {
      this.$emit("update:completed", value);
    },
  },
};
</script>

<style scoped>
.list-btns {
  display: flex;
  justify-content: space-between;
}

.edit-btns {
  display: flex;
  gap: 10px;
}
</style>
