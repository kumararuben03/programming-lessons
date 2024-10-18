<template>
  <v-app>
    <v-main>
      <v-container class="fill-height">
        <v-responsive class="mx-auto border-sm" max-width="500">
          <h1 class="text-center my-5">Login Page</h1>

          <v-form fast-fail @submit.prevent class="pa-4">
            <v-text-field
              label="username"
              prepend-inner-icon="mdi-email-outline"
              placeholder="johndoe@gmail.com"
              type="email"
            ></v-text-field>

            <v-btn class="mt-2" type="submit" color="#013D5A" block
              >Submit</v-btn
            >
          </v-form>
        </v-responsive>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
//
</script>
