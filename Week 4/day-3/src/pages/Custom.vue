<template>
  <div class="pa-5">
    <ul>
      <li v-for="(item, index) in items" :key="index" v-highlight-on-click>
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
    };
  },
};
</script>
