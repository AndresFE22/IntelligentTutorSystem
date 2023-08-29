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


//---------------------Componentes--------------------//


import Home from "./components/Home.vue";
import login from "./components/loginU.vue"
import register from "./components/registerU.vue"
import profile from "./components/ProfileUser.vue"
import DiagnosisState from "./components/diagnosisState.vue";
import DiagnosisStyles from "./components/diagnosisStyles.vue"; 
import responseStyles from "./components/responseStyles.vue"
import ActivityGlobal from "./components/ResourcesComponent/ResourcesViewGlobal"
import ActivitySequential from "./components/ResourcesComponent/ResourcesViewSequential.vue"
import diagnosisStateEvaluation from "./components/diagnosisStateEvaluation.vue"
import ActivityITS from "./components/ActivityITS.vue"


//------------------------//--------------------------------//



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
    path: "/profile",
    name: "profile",
    component: profile,
    meta: { requiresAuth: true }
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

router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  console.log('isLoggedIn:', isLoggedIn); // Agrega este console.log para verificar 
    if ( isLoggedIn && to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.state.auth) {
      next();
    } else {
      next({ name: "Home" });
    }
  } else {
    next();
  }
});


const vuetify = new Vuetify();

new Vue({
  router,
  vuetify,  
  store,
  render: h => h(App),
}).$mount('#app');


