<template>
  <v-app>
    <v-main>
      <v-container class="fill-height" >
        <v-responsive class="mx-auto border-sm bg-light-blue-darken-4" max-width="1000">

          <h1 class="text-center my-5">Registration Page</h1>

          <v-form fast-fail @submit.prevent class="pa-4">
            <h2 class="mb-2">Student Information</h2>

            <v-row align="center">

              <v-col cols="4">
                <v-text-field
              label="First Name"
              prepend-inner-icon="mdi-account"
              type="text"
              ></v-text-field>
              </v-col>

              <v-col cols="4">
                <v-text-field
              label="Middle Name"
              prepend-inner-icon="mdi-account"
              type="text"
              ></v-text-field>
              </v-col>

              <v-col cols="4">
                <v-text-field
              label="Last Name"
              prepend-inner-icon="mdi-account"
              type="text"
              ></v-text-field>
              </v-col>
            </v-row>

            <v-row align="center">
              <v-col cols="6">
                <v-text-field
                label="Birth Date"
                prepend-inner-icon="mdi-cake-variant"
                type="date">

                </v-text-field>
              </v-col>

              <v-col cols="6">
                <v-text-field
                label="Student ID"
                prepend-inner-icon="mdi-credit-card"
                >
                </v-text-field>
              </v-col>
            </v-row>

            <v-row align="center">
              <v-col cols="3">
                <p>Gender:</p>
                <v-radio-group inline>
                  <v-radio label="Male" value="male"></v-radio>
                  <v-radio label="Female" value="female"></v-radio>
                </v-radio-group>
              </v-col>

              <v-col cols="9">
                <p>Choose one study area:</p>
                <v-radio-group inline>
                  <v-radio label="IT" value="it"></v-radio>
                  <v-radio label="Data Science" value="data-science"></v-radio>
                  <v-radio label="Arts and Social Science" value="arts-social"></v-radio>
                  <v-radio label="Engineering" value="engineering"></v-radio>
                  <v-radio label="Finance" value="finance"></v-radio>
                  <v-radio label="Economy" value="economy"></v-radio>
                  <v-radio label="Science" value="science"></v-radio>
                </v-radio-group>
              </v-col>
            </v-row>

            <h2 class="mb-2">Address</h2>
            <v-text-field
              label="Street Address"
              prepend-inner-icon="mdi-map-marker"
              type="text"
              ></v-text-field>

              <v-row align="center">
              <v-col cols="6">
                <v-text-field
                label="City"
                prepend-inner-icon="mdi-map-marker">

                </v-text-field>
              </v-col>

              <v-col cols="6">
                <v-text-field
                label="Street/Province"
                prepend-inner-icon="mdi-map-marker"
                >
                </v-text-field>
              </v-col>
            </v-row>

            <v-row align="center">
              <v-col cols="6">
                <v-text-field
                label="Country"
                prepend-inner-icon="mdi-map-marker">

                </v-text-field>
              </v-col>

              <v-col cols="6">
                <v-text-field
                label="ZIP Code"
                prepend-inner-icon="mdi-map-marker"
                >
                </v-text-field>
              </v-col>
            </v-row>

            <h2 class="mb-2">Contact Info</h2>
            <v-row align="center">
              <v-col cols="6">
                <v-text-field
                label="Email"
                prepend-inner-icon="mdi-email"
                type="email">

                </v-text-field>
              </v-col>

              <v-col cols="6">
                <v-text-field
                label="Student ID"
                prepend-inner-icon="mdi-phone"
                >
                </v-text-field>
              </v-col>
            </v-row>
            
            <h2 class="mb-2">Upload Transcript</h2>
            <v-row align="center">
              <v-col cols="1">
                <v-icon>
                  mdi-paperclip
                </v-icon>
              </v-col>

              <v-col cols="11">
                <v-text-field
                label="Transcript in PDF format"
                >
                </v-text-field>
              </v-col>
            </v-row>

            <h2 class="mb-2">Remarks</h2>
            <v-textarea 
              label="Additional Comments/Feedback"
              name="input-7-1"
              variant="filled"
              auto-grow
    >       </v-textarea>

      <v-btn class="mt-2" type="submit" color="blue-darken-3" block>Submit</v-btn>
          </v-form>
        </v-responsive>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
  //
</script>
