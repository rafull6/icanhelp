import Vue from "vue";
import Router from "vue-router";
import Login from "./components/Login/Login.vue";
import Mobile from "./components/Mobile/Mobile.vue";
import Dashboard from "./components/Dashboard/Dashboard.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: Dashboard
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/mobile",
      name: "mobile",
      component: Mobile
    },
    // {
    //   path: "/about",
    //   name: "about",
    //   component: () =>
    //     import(/* webpackChunkName: "about" */ "./views/About.vue")
    // }
  ]
});
