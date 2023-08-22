<template>
  <div class="login-container">
    <div class="login-card">
      <h1 class="login-title">Iniciar sesión</h1>
      <form class="login-form">
        <div class="form-group">
          <label for="username">Usuario</label>
          <input v-model="user" id="username" class="form-control" placeholder="Ingrese su usuario" />
        </div>
        <div class="form-group">
          <label for="password">Contraseña</label>
          <input v-model="password" id="password" class="form-control" type="password" placeholder="Ingrese su contraseña" />
        </div>
        <button @click="login" class="login-button">Iniciar sesión</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "LoginU",
  data() {
    return {
      user: '',
      password: '',
    };
  },
  methods: {
    login() {
      axios.post('/api/login', {
        username: this.user,
        password: this.password
      })
      .then(response => {
        console.log(response.data.message);
      })
      .catch(error => {
        console.error(error);
      });
    }
  }
};
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
