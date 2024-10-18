<template>
  <v-container>
    <v-row>
      <v-col v-for="post in getPosts" :key="post.id" cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>{{ post.title }}</v-card-title>
          <v-card-text>
            {{ post.body }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { usePostStore } from "./../stores/posts";

const postStore = usePostStore();
const getPosts = computed(() => postStore.getPosts);

onMounted(postStore.fetchPosts);
</script>
