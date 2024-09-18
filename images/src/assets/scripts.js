export default {
  data() {
    return {
      images: [
        {
          url: "https://placehold.co/600x400/000000/FFF",
          desc: "Nice landscape",
        },

        {
          url: "https://placehold.co/600x400/orange/white",
          desc: "Awesome view",
        },

        {
          url: "https://placehold.co/600x400/blue/white",
          desc: "Blue Ocean",
        },
      ],
      isOpened: false,
      selectedImage: null,
    };
  },

  methods: {
    openDialog(image) {
      this.selectedImage = image;
      this.isOpened = true;
      console.log(this.selectedImage, this.isOpened);
    },

    closeDialog() {
      this.isOpened = false;
    },
  },
};
