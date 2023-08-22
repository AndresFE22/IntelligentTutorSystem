<template>
  <div class="register-container">
    <div class="register-card">
      <h1 class="register-title">Registro</h1>
      <form class="register-form">
        <div class="form-group">
          <label for="name">Nombre Completo</label>
          <input v-model="name" id="name" class="form-control" placeholder="Ingrese su nombre completo" />
        </div>
        <div class="form-group">
          <label for="username">Usuario</label>
          <input v-model="user" id="username" class="form-control" placeholder="Ingrese su usuario" />
        </div>
        <div class="form-group">
          <label for="password">Contraseña</label>
          <input v-model="password" id="password" class="form-control" type="password" placeholder="Ingrese su contraseña" />
        </div>
        <button @click="register" class="register-button">Registrar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      user: '',
      password: '',
    };
  },
  methods: {
    register() {
      axios.post('api/register', {
        name: this.name,
        user: this.user,
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
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 45vh;
}

.register-card {
  background-color: #fff;
  border-radius: 10px;
  padding: 30px;
  width: 100%;
  max-width: 400px;
}

.register-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.register-form {
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

.register-button {
  background-color: #0084ff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.register-button:hover {
  background-color: #0064cc;
}
</style>
