<template>
  <div class="text-center pa-4">
    <v-card
      v-for="image in images"
      :key="image.url"
      max-width="600"
      max-height="400"
      class="image-grid"
    >
      <v-img
        :src="image.url"
        @click="openDialog(image)"
        :lazy-src="image.url"
      />
    </v-card>

    <v-container>
      <v-dialog v-model="isOpened" max-width="500">
        <v-card>
          <v-img :src="selectedImage.url" />
          <v-card-text>{{ selectedImage.desc }}</v-card-text>
          <v-btn class="ms-auto" text="Close" @click="closeDialog"></v-btn>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>

<script src="./assets/scripts.js"></script>
<style src="./assets/styles.css"></style>
