<template>
  <v-app>
    <v-main>
      <v-checkbox
        label="Show Out of Stock"
        v-model="showOutOfStock"
      ></v-checkbox>

      <v-row>
        <v-col
          cols="12"
          sm="6"
          md="4"
          v-for="item in availableItems"
          :key="item.id"
        >
          <v-card :class="{ 'border-success': item.inStock }">
            <v-card-title
              :style="{ backgroundColor: priceColor(item.price) }"
              >{{ item.name }}</v-card-title
            >
            <v-card-text>{{ item.price }}</v-card-text>
            <v-card-text v-model="showOutOfStock">{{
              item.inStock
            }}</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { id: 1, name: "Product A", price: 25.99, inStock: true },
        { id: 2, name: "Product B", price: 12.5, inStock: false },
        { id: 3, name: "Product C", price: 39.95, inStock: true },
      ],
      showOutOfStock: false,
      borderColor: "",
      headerColor: "",
    };
  },

  methods: {
    priceColor(price) {
      const maxPrice = 50;
      const hue = (1 - price / maxPrice) * 120;
      return `hsl(${hue}, 60%, 50%)`;
    },
  },

  computed: {
    availableItems() {
      if (this.showOutOfStock) {
        return this.items;
      } else {
        return this.items.filter((item) => item.inStock);
      }
    },
  },
};
</script>

<style>
.border-success {
  border: 2px solid lightgreen !important;
}
</style>
