import Vue from "vue";
import VueGeolocation from 'vue-browser-geolocation';
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.use(VueGeolocation);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
