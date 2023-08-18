<template>
  <div class="container">
    <h1>Inicio de sesión</h1>
    <v-form @submit="login">
      <v-text-field v-model="username" label="Nombre de usuario"></v-text-field>
      <v-text-field v-model="password" label="Contraseña" type="password"></v-text-field>
      <v-btn dark type="submit">Iniciar sesión</v-btn>
    </v-form>
    <br>
    <div v-if="showError" class="error-message">
      Usuario o contraseña incorrectos
    </div>
  </div>
</template>

<style>
.container {
  margin-top: 4%;
  overflow: hidden;
}

.error-message {
  background-color: #f44336;
  color: white;
  padding: 10px;
  border-radius: 4px;
  text-align: center;
}

@media (max-width: 600px) {
  .container {
    margin-top: 12%;
  }
}
</style>

<script>


export default {
  data() {
    return {
      username: '',
      password: '',
      showError: false,
    };
  },
  methods: {
    login() {
      if (this.username === 'admin' && this.password === 'admin123') {
        this.$router.push('/Campos/ingresar-palabra');
      } else {
        this.showError = true;
        setTimeout(() => {
          this.showError = true;
        }, 2000);
      }
    },
  },
  name: 'ConfigLogin'
};
</script>
