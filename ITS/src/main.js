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

import axios from 'axios'
router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    try {
      console.log('Before axios.get');
      const response = await axios.get('api/check-auth'); // Cambia la ruta según tu implementación
      console.log('After axios.get', response.data);
      if (response.data.isAuthenticated) {
        console.log('User is authenticated');
        next({ name: 'DiagnosisState' });
      } else {
        console.log('User is not authenticated');
        next({ name: 'Home' });
      }
    } catch (error) {
      console.error('Error while checking authentication:', error);
      next({ name: 'Home' }); 
    }
  } else {
    console.log('Route does not require authentication');
    next();
  }
});


new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app');
