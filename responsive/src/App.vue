<template>
  <v-app>
    <v-main>
      <v-row>
        <v-col
        v-for="n in 60"
        :key="n"
        cols="3"
        sm="3"
        md="2"
        lg="1">

        <v-img 
        :src= "`https://picsum.photos/500/300?image=${n*5+10}`"
        aspect-ratio="1"
        class="bg-grey-lighten-2"
        cover
        >

        </v-img>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script setup>
  //
</script>
