<template>
  <v-tabs v-model="activeTab">
    <v-tab value="tab1">Tab 1</v-tab>
    <v-tab value="tab2">Tab 2</v-tab>

    <v-tab-items v-model="activeTab">
      <v-tab-item value="tab1">
        <keep-alive>
          <TabOne v-if="activeTab === 'tab1'" tabName="tab1" />
        </keep-alive>
      </v-tab-item>

      <v-tab-item value="tab2">
        <keep-alive>
          <TabOne v-if="activeTab === 'tab2'" tabName="tab2" />
        </keep-alive>
      </v-tab-item>
    </v-tab-items>
  </v-tabs>
</template>

<script>
import TabOne from "./../components/TabOne.vue";

export default {
  data() {
    return {
      activeTab: "tab1",
      timer: null,
    };
  },

  components: {
    TabOne,
  },

  methods: {
    startTimer() {
      this.timer = setInterval(() => {
        this.activeTab = this.activeTab === "tab1" ? "tab2" : "tab1";
      }, 2000);
    },

    clearTimer() {
      if (this.timer) {
        clearInterval(this.timer);
        this.timer = null;
      }
    },
  },

  watch: {
    activeTab(newTab, oldTab) {
      this.startTimer();
    },
  },

  mounted() {
    this.startTimer();
  },

  beforeDestroy() {
    this.clearTimer();
  },
};
</script>
