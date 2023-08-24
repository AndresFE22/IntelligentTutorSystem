import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import store from './store'
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
    meta: { requiresAuth: true }
  },
  {
    path: "/DiagnosisStyles",
    name: "DiagnosisStyles",
    component: DiagnosisStyles,
    meta: { requiresAuth: true }    
  },
  {
    path: "/ResponseStyles",
    name: "ResponseStyles",
    component: responseStyles,
    meta: { requiresAuth: true }
  },
  {
    path: "/ActivityGlobal",
    name: "ActivityGlobal",
    component: ActivityGlobal,
    meta: { requiresAuth: true }
  },
  {
    path: "/ActivitySequential",
    name: "ActivitySequential",
    component: ActivitySequential,
    meta: { requiresAuth: true }
  },
  {
    path: "/diagnosisStateEvaluation",
    name: "diagnosisStateEvaluation",
    component: diagnosisStateEvaluation,
    meta: { requiresAuth: true }
  },
  {
    path: "/ActivityITS",
    name: "ActivityITS",
    component: ActivityITS,
    meta: { requiresAuth: true }
  }
];

const router = new VueRouter({
  mode: 'history',
  routes,
});
const vuetify = new Vuetify();

const app = new Vue({
  router,
  vuetify,
  store,
  render: h => h(App),
}).$mount('#app');

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !app.$store.state.isAuthenticated) {
    console.log('User is not authenticated');
    next({ name: 'Home' });
  } else {
    console.log('User is authenticated');
    next();
  }
});
