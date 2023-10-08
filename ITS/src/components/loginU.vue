<template>
  <div class="login-container">
    <div class="login-card">
      <h1 class="login-title">log in</h1>
      <form class="login-form">
        <div class="form-group">
          <label for="username">user</label>
          <input v-model="user" id="username" class="form-control" placeholder="Enter your username" />
        </div>
        <div class="form-group">
          <label for="password">password</label>
          <input v-model="password" id="password" class="form-control" type="password" placeholder="Enter your password" />
        </div>
        <button @click="onSubmit" class="login-button">log in</button>
      </form>
      <button @click="checkAuthStatus">Verificar Estado de Autenticación</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';


export default {
  name: "LoginU",
  data() {
    return {
      user: '',
      password: '',
    };
  },
  computed: {
  ...mapState(['auth'])
},


  methods: {
    async onSubmit() {
  try {
    const response = await axios.post('/api/login', {
      user: this.user,
      password: this.password
    });

    console.log(response.data.message);
    console.log(response.data.user.id);
    if (response.data.message === 'Login successful') {
      localStorage.setItem('isLoggedIn', 'true')
      const userId = response.data.user.id
      const userData = response.data.user
      this.$store.commit('setUserId', userId)
      this.$store.commit('setUserData', userData)
      localStorage.setItem('userId', userId)
      await this.$store.dispatch('doLogin', this.user);

      const estadoResponse = await axios.get(`/api/stateVerified/${userId}`);
      const estadoData = estadoResponse.data;
      console.log(estadoData);

      if (estadoData.TestTopic === 0 || estadoData.TestTopic === null) {
        this.$router.push({ name: 'DiagnosisState' });
      } else if (estadoData.TestStyle === 0 || estadoData.TestStyle === null) {
        this.$router.push({ name: 'DiagnosisStyles' });
      } else {
        this.$router.push({ name: 'ActivityITS' });
      }
    }
  } catch (error) {
    console.error(error);
  }
},

  checkAuthStatus() {
      console.log('Estado de autenticación:', this.auth);
    }
},
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 45vh;
}

.login-card {
  background-color: #fff;
  border-radius: 10px;
  padding: 30px;
  width: 100%;
  max-width: 400px;
}

.login-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.login-button {
  background-color: #0084ff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #0064cc;
}
</style>
