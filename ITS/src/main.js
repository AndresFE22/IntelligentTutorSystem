import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import '@mdi/font/css/materialdesignicons.css';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import 'vuetify/dist/vuetify.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Home from "./components/Home.vue";
import login from "./components/loginU.vue"
import register from "./components/registerU.vue"
import DiagnosisState from "./components/diagnosisState.vue";
import DiagnosisStyles from "./components/diagnosisStyles.vue"; 
import responseStyles from "./components/responseStyles.vue"
import ActivityGlobal from "./components/ResourcesComponent/ResourcesViewGlobal"
import ActivitySequential from "./components/ResourcesComponent/ResourcesViewSequential.vue"
import diagnosisStateEvaluation from "./components/diagnosisStateEvaluation.vue"
import ActivityITS from "./components/ActivityITS.vue"




Vue.config.productionTip = false;

Vue.use(VueRouter);
Vue.use(Vuetify);
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "login",
    component: login,
  },
  {
    path: "/register",
    name: "register",
    component: register,
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
  },
  {
    path: "/ActivityGlobal",
    name: "ActivityGlobal",
    component: ActivityGlobal
  },
  {
    path: "/ActivitySequential",
    name: "ActivitySequential",
    component: ActivitySequential
  },
  {
    path: "/diagnosisStateEvaluation",
    name: "diagnosisStateEvaluation",
    component: diagnosisStateEvaluation
  },
  {
    path: "/ActivityITS",
    name: "ActivityITS",
    component: ActivityITS
  }
];

const router = new VueRouter({
  mode: 'history',
  routes,
});
const vuetify = new Vuetify();


new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app');
