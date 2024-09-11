<template>

  <v-app>
    <v-app-bar class="px-3 text-center">

      <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template>

      <v-app-bar-title>
      <v-icon>mdi-car-cog</v-icon>
      ABX Workshop
    </v-app-bar-title>

    <v-btn icon>
      <v-icon>mdi mdi-web</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>mdi mdi-login</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>mdi mdi-dots-vertical</v-icon>
    </v-btn>
    </v-app-bar>

    <v-main>
  <v-row>
    <v-col cols="12">
  <v-carousel height="800">
  <v-carousel-item
    src="./assets/images/carousel-1.jpg"
    cover
  ></v-carousel-item>

  <v-carousel-item
    src="./assets/images/carousel-2.jpg"
    cover
  ></v-carousel-item>

  <v-carousel-item
    src="./assets/images/carousel-3.jpg"
    cover
  ></v-carousel-item>
</v-carousel>
</v-col>
</v-row>

  <v-row>
    <v-col cols="12">
      <v-tabs
      class="bg-grey-lighten-2 opacity-90"
      slider-color="grey-darken-3"
      v-model="tab"
      align-tabs="center"
      >
      <v-tab :value="1"><h2 class="mx-5">Home</h2></v-tab>
      <v-tab :value="2"><h2 class="mx-5">Get a Quote</h2></v-tab>
      <v-tab :value="2"><h2 class="mx-5">Booking</h2></v-tab>
      <v-tab :value="2"><h2 class="mx-5">Blog</h2></v-tab>
      <v-tab :value="3"><h2 class="mx-5">Contact</h2></v-tab>
    </v-tabs>
    </v-col>
  </v-row>

  <v-row class="text-center">
    <v-col cols="12">
      <h1>Your One Stop Auto Service Center</h1>
      <h4>Automative services and maintenance that keeps your vehicle driving</h4>
    </v-col>
  </v-row>

  <br></br>

  <v-row class="mx-3">
    <v-col cols="4">
      <v-img
      width="640"
      height="360"
      src="./assets/images/carousel-3.jpg"
      class="ma-auto"
      cover></v-img>
    </v-col>

    <v-col cols="8">
     <p class="text-justify text-h6">
      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
     </p>

     <br>

     <p class="text-justify text-h6">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

     <br>

     
    </v-col>
  </v-row>
  <v-row class="mb-3 mx-3">
    <v-col cols="3">
      <v-card 
      max-height="600"
      >
      <v-img
      height="400"
      src="./assets/images/image-1.jpg"
      cover></v-img>

      <v-card-title class="text-center text-uppercase">Motor Services</v-card-title>

      <v-card-text class="text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>
    </v-card>
    </v-col>

    <v-col cols="3">
      <v-card 
      max-height="600"
      >
      <v-img
      height="400"
      src="./assets/images/image-2.jpg"
      cover></v-img>

      <v-card-title class="text-center text-uppercase">Paint Job</v-card-title>

      <v-card-text class="text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>
    </v-card>
    
    </v-col>

    <v-col cols="3">
      <v-card 
      max-height="600"
      >
      <v-img
      height="400"
      src="./assets/images/image-3.jpg"
      cover></v-img>

      <v-card-title class="text-center text-uppercase">Services</v-card-title>

      <v-card-text class="text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>
    </v-card>
    </v-col>

    <v-col cols="3">
      <v-card 
      max-height="600"
      >
      <v-img
      height="400"
      src="./assets/images/image-4.jpg"
      cover></v-img>

      <v-card-title class="text-center text-uppercase">Tyre Services</v-card-title>

      <v-card-text class="text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>
    </v-card>
    </v-col>
  </v-row>

  <v-row class="text-center">
    <v-col cols="12">
      <h2>4 Simple Steps to Service Your Car</h2>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="12">
      <v-timeline side="end">
        <v-timeline-item size="small" width="700">
          <v-alert color="success">
            <strong>Step 1: </strong>Select a service.
          </v-alert>
        </v-timeline-item>

        <v-timeline-item size="small" width="700">
          <v-alert color="success">
            <strong>Step 2: </strong>Schedule your service or walk-in.
          </v-alert>
        </v-timeline-item>

        <v-timeline-item size="small" width="700">
          <v-alert color="success">
            <strong>Step 3: </strong>Track the status of your service and receive updates on proposed work and repairs carried out.
          </v-alert>
        </v-timeline-item>

        <v-timeline-item size="small" width="700">
          <v-alert color="success">
            <strong>Step 4: </strong>Make payment and collect your car.
          </v-alert>
        </v-timeline-item>
      </v-timeline>
    </v-col>
  </v-row>
    </v-main>
    <v-footer height="60" class="bg-blue-grey-darken-4" app>
      <div class="mx-auto">
        {{ new Date().toDateString() }} - <strong>ABX Workshop</strong>
      </div>

      <div class="d-flex flex-row-reverse">
        <v-btn icon class="mx-2">
          <v-icon size="25" >mdi mdi-youtube</v-icon>
        </v-btn >
        <v-btn icon class="mx-2">
          <v-icon size="25">mdi mdi-instagram</v-icon>
        </v-btn >
        <v-btn icon class="mx-2">
          <v-icon size="25">mdi mdi-facebook</v-icon>
        </v-btn>
      </div>
    </v-footer>
  </v-app>
</template>

<script setup>
  //
</script>
