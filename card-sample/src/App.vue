<template>
  <v-app>
    <v-main>
      <v-container class="fill-height">
        <v-card 
        class="mx-auto pa-2" 
        max-width="500">
          <v-img 
          width="500" 
          height="300" 
          src="./assets/petronas_tower.jpg" 
          cover>
        </v-img>
          <v-card-title class="text-center font-weight-bold">
            PETRONAS Twin Towers
          </v-card-title>

          <v-card-subtitle class="text-center font-weight-bold">
            Malaysia Landmark Building
          </v-card-subtitle>

          <v-card-text class="text-justify">
            The Petronas Twin Towers, located in Kuala Lumpur,
            Malaysia, are iconic skyscrapers that were once the
            tallest buildings in the world from 1998 to 2004.
          </v-card-text>

          <v-card-actions>
            <v-btn
            append-icon="mdi-chevron-right" 
            color="red-lighten-2" 
            text="Explore" 
            variant="tonal" 
            block
            class="text-button">
          </v-btn>
          </v-card-actions>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  //
</script>
