import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import "./style.css";

const app = createApp(App);

app.use(createPinia());

app.config.errorHandler = (err) => {
  console.error("Global Error:", err);
};

app.mount("#app");