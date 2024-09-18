<template>
  <div class="profile-card">
    <img v-bind:src="user.image" v-bind:alt="user.name" class="profile-image" />
    <h2 v-bind:class="{ highlight: isHighlighted }">{{ user.name }}</h2>
    <p>Age: {{ user.age }}</p>
    <button v-bind:disabled="!user.isActive">Send Message</button>
    <br />
    <button @click="toggleHighlight">
      {{ isHighlighted ? "Remove Highlight" : "Highlight" }}
    </button>
  </div>

  <input type="text" v-model="message" />
  <p>Current message: {{ message }}</p>
</template>

<script>
export default {
  setup() {
    const message = ref("");
    const showGreeting = ref(true);
    const items = ref(["Item 1", "Item 2", "Item 3"]);
    const imageUrl = ref("https://picsum.photos/200/300");
    const bgColor = ref("lightblue");
    const fontColor = ref("red");

    const handleClick = () => {
      console.log("Button clicked");
    };

    return {
      message,
      showGreeting,
      items,
      imageUrl,
      bgColor,
      fontColor,
    };
  },

  data() {
    return {
      user: {
        name: "John Doe",
        age: 20,
        image: "https://picsum.photos/200/300",
        isActive: true,
      },
      isHighlighted: false,
    };
  },
  methods: {
    toggleHighlight() {
      this.isHighlighted = !this.isHighlighted;
    },
  },
};
</script>

<style>
.highlight {
  background-color: yellow;
}
</style>
