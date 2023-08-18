<template>
    <div class="campos">
      <h1>EDITAR ORACION</h1>
      <div class="form-container">
        <v-text-field v-model="nuevaInformacion" label="Digite su información" class="text"></v-text-field>
        <v-text-field v-model="nuevoSignificado" label="Digite su significado" class="text"></v-text-field>
        <v-btn @click="editarInfo">Editar información</v-btn>
        <br>
        <router-link to="/Campos/editar-info"><v-btn>Regresar</v-btn></router-link>
        <br>
          <br>
          <div v-if="mensaje" class="mensaje">{{ mensaje }}</div>
      </div>
    </div>
  </template>
  
  <style scoped>
    .mensaje {
    background-color: rgb(13, 126, 255);
    color: white;
    padding: 10px;
    border-radius: 20px;
    }
  .campos {
    margin-top: 15px;
  }
  
  .form-container {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .form-container .text {
    width: 50%;
  }
  
  @media (max-width: 600px) {
    .form-container .text {
      width: 70%;
    }
  }
  </style>
      
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        nuevaInformacion: '',
        nuevoSignificado: '',
        mensaje: ""

      };
    },
    
    methods: {
      editarInfo() {
        const id = this.$route.params.id;
  
        const datos = {
          informacion: this.nuevaInformacion,
          significado: this.nuevoSignificado
        };
  
        axios.put(`https://cuentaapi.pythonanywhere.com/apik/info/${id}`, datos)
          .then(response => {
            console.log(response.data);
            this.mensaje = response.data.message;
          setTimeout(() => {
            this.mensaje = "";
          }, 3000
         )
            this.nuevaInformacion = '';
            this.nuevoSignificado = '';
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  };
  </script>
  