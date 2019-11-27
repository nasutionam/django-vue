import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Example from "../views/Example.vue";
import About from "../views/About.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/example",
    name: "example",
    component: Example
  },
  {
    path: "/about",
    name: "about",
    component: About
  }
];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL,
  routes
});

export default router;
