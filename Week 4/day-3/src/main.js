/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from "@/plugins";

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

const app = createApp(App);

app.directive("color-on-hover", {
  mounted(el, binding) {
    el.style.transition = "color 0.3s";

    el.addEventListener("mouseover", () => {
      el.style.color = binding.value || "red";
    });

    el.addEventListener("mouseout", () => {
      el.style.color = "";
    });
  },
});

app.directive("highlight-on-click", {
  mounted(el, binding) {
    console.log(el);
    el.style.transition = "background-color 0.3s";

    el.addEventListener("click", (e) => {
      const highlightedElement = document.querySelector(".highlighted");
      if (highlightedElement) {
        highlightedElement.style.backgroundColor = "";
        highlightedElement.classList.remove("highlighted");
      }

      e.target.style.backgroundColor = binding.value || "darkblue";
      e.target.classList.add("highlighted");
    });
  },
});

registerPlugins(app);

app.mount("#app");
