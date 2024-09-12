<template>
  <v-app>
    <v-main>
      <v-container class="fill-height">
        <v-row>
          <v-col cols="6">
            <LineChart/>
          </v-col>

            <v-col cols="6">
            <BarChart/>
          </v-col>
        </v-row>

      <v-row>
        <v-col cols="4">
          <PieChart/>
      </v-col>

        <v-col cols="4">
          <DonutChart/>
      </v-col>

        <v-col cols="4">
          <RadarChart/>
      </v-col>

      </v-row>
     
      </v-container>

    </v-main>
  </v-app>
</template>

<script setup>

  //
</script>
