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
