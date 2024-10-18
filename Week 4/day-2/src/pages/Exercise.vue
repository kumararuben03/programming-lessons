<template>
  <v-container>
    <v-row>
      <v-col v-for="user in users" :key="user.id" cols="12" sm="6" md="4">
        <v-card>
          <v-card-item>
            <v-card-title>{{ user.name }}</v-card-title>
            <v-card-text>{{ user.email }}</v-card-text>
            <v-card-text>{{ user.username }}</v-card-text>
            <v-card-text>{{ user.phone }}</v-card-text>
            <v-card-text>{{ user.website }}</v-card-text>
          </v-card-item>
        </v-card>
      </v-col>
    </v-row>

    <Carousel />
    <Message />
  </v-container>
</template>

<script>
import Carousel from "@/components/Carousel.vue";
import Message from "@/components/Message.vue";

export default {
  data() {
    return {
      users: [],
    };
  },

  components: {
    Carousel,
    Message,
  },

  beforeCreated() {
    console.log("beforeCreated hook executed");
  },

  created() {
    console.log("created hook executed");
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => {
        this.users = data;
        console.log("Fetched items: ", this.users);
      })
      .catch((error) => console.error("Error fetching items: ", error));
  },
};
</script>
