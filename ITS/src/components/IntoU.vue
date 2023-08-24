<template>
  <v-card class="auth-card" elevation="10">
    <v-card-text>
      <div class="content-container">
        <div v-if="isLogin" @submit.prevent="login">
          <login />
        </div>
        <div v-else @submit.prevent="register">
          <register />
        </div>
        <input type="button" class="toggle-button" @click="toggleMode" :value="isLogin ? 'Registrarse aquí' : 'Iniciar sesión aquí'" />
      </div>
      
    </v-card-text>
  </v-card>
</template>

<script>
import login from "./loginU.vue";
import register from "./registerU.vue";

export default {
  data() {
    return {
      isLogin: true,
    };
  },
  components: {
    login,
    register,
  },
  methods: {
    toggleMode() {
      this.isLogin = !this.isLogin;
    },
  },
};
</script>

<style scoped>
.auth-card {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  padding: 30px;
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-height: 500px;
  justify-content: center;
}

.auth-card h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.content-container {
  width: 100%;
  overflow: hidden;
}

.auth-card v-form {
  width: 100%;
}

.toggle-button{
 text-decoration: underline;
 font-weight: bold;
} 

.toggle-button:hover{
 color: rgb(0, 140, 255);
 transform: scale(0.99);
 transition: all 0.5s ease;
} 

</style>
