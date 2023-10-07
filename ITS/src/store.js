import Vue from "vue";
import Vuex from "vuex";


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: null,
    auth: false,
    userId: localStorage.getItem('userId') || null,
    userData: []
  },
  mutations: {
    setUserData(state, userData) {
      state.userData = userData
    },
    doLogin(state, username) {
      state.auth = true;
      state.username = username;
    },
    setUserId(state, userId) {
      state.userId = userId
      localStorage.setItem('userId', userId)
    },
    clearUserId(state) {
      state.userId = null
      localStorage.removeItem('userId')
    },
    doLogout(state) {
      state.auth = false;
      state.username = null;
    }
  },
  actions: {
    doLogin({ commit }, username) {
      commit("doLogin", username);
    },
    doLogout({ commit }) {
      commit("doLogout");
    }
  },

});
