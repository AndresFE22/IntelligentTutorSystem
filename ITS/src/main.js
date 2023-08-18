import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import '@mdi/font/css/materialdesignicons.css';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import 'vuetify/dist/vuetify.css';
import Home from "./components/Home.vue";
import DiagnosisState from "./components/diagnosisState.vue";
import DiagnosisStyles from "./components/diagnosisStyles.vue"; 
import responseStyles from "./components/responseStyles.vue"

Vue.config.productionTip = false;

Vue.use(VueRouter);
Vue.use(Vuetify);


const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/DiagnosisState",
    name: "DiagnosisState",
    component: DiagnosisState,
  },
  {
    path: "/DiagnosisStyles",
    name: "DiagnosisStyles",
    component: DiagnosisStyles,
  },
  {
    path: "/ResponseStyles",
    name: "ResponseStyles",
    component: responseStyles
  }
];

const router = new VueRouter({
  routes,
});

const vuetify = new Vuetify();


new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app');
