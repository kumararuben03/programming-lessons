import { defineStore } from "pinia";

export const usePostStore = defineStore("post", {
  state: () => ({
    posts: [],
  }),
  getters: {
    getPosts: (state) => state.posts,
  },
  actions: {
    async fetchPosts() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );
        const data = await response.json();
        this.posts = data;
      } catch (err) {
        console.error("Error fetching posts:", err);
      }
    },
  },
});
