<template>
  <v-app>
    <v-main>
      <v-dialog max-width="500" max-height="80vh">
        <template v-slot:activator="{ props: activatorProps }">
          <v-btn
            v-bind="activatorProps"
            color="surface-variant"
            text="Open Dialog"
            variant="flat"
          ></v-btn>
        </template>

        <template v-slot:default="{ isActive }">
          <v-card
    class="mx-auto pa-2 border-sm"
    width="400"
    height="400"
  >
    <v-card-title>Kuala Lumpur</v-card-title>
    <v-card-subtitle>Tues, 01:30 PM, Mostly Sunny</v-card-subtitle>
        <br>
    <v-card-text class="py-0">
      <v-row align="center" no-gutters>
        <v-col
          class="text-h2"
          cols="6 pl-2 my-2"
        >
          30&deg;C
        </v-col>

        <v-col class="text-right pr-10" cols="6">
          <v-icon
            color="deep-orange-darken-1"
            icon="mdi-weather-sunny"
            size="88"
          ></v-icon>
        </v-col>
      </v-row>
    </v-card-text>

    <v-card-text class="mt-9">
      <v-row align="center" no-gutters>
        <v-col
          class="text-h6 text-center"
          cols="6"
        >
        <v-card-subtitle>
          <v-icon
            icon="mdi-weather-pouring"
            size="50"
            >
          </v-icon>
          <br>
          2% Precipitation
        </v-card-subtitle>
          
        </v-col>

        <v-col class="text-center" cols="6">
          <v-card-subtitle>
          <v-icon
            icon="mdi-weather-windy"
            size="50"
          ></v-icon>
          <br>
          20km/h Wind
        </v-card-subtitle>
        </v-col>
      </v-row>
    </v-card-text>

    <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn
          text="Close Dialog"
          @click="isActive.value = false"
          variant="outlined"
        ></v-btn>
      </v-card-actions>
  </v-card>
        </template>
      </v-dialog>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
</script>

