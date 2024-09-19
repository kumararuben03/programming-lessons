<template>
  <div class="responsive">
    <v-row>
      <v-col cols="12" md="6" sm="4" href="#">Home</v-col>
      <v-col cols="12" md="6" sm="4" href="#">About</v-col>
      <v-col cols="12" md="6" sm="4" href="#">Services</v-col>
      <v-col cols="12" md="6" sm="4" href="#">Contact</v-col>
    </v-row>
    <div class="container">
      <v-row>
        <v-col cols="12" md="6" sm="4">Card 1</v-col>
        <v-col cols="12" md="6" sm="4">Card 2</v-col>
        <v-col cols="12" md="6" sm="4">Card 3</v-col>
        <v-col cols="12" md="6" sm="4">Card 4</v-col>
      </v-row>
    </div>
  </div>
</template>

<script></script>

<style>
nav {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin: 20px 0;
}

nav a {
  margin: 10px;
  padding: 10px 15px;
  background: #f2f2f2;
  color: #333;
  text-decoration: none;
  border-radius: 5px;
}

.responsive {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.container {
  max-width: 1200px;
  width: 100%;
  margin: auto;
  padding: 20px;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.card {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 15px;
  flex: 1;
}

@media (min-width: 600px) {
  nav {
    justify-content: space-around;
  }

  .content {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .card {
    flex: 1 1 calc(33.333% - 20px);
  }
}

@media (min-width: 900px) {
  .card {
    flex: 1 1 calc(25% - 20px);
  }
}
</style>
