<template>
    <div>
      <h1>Datos</h1>
      <v-text-field v-model="nuevoDato" label="Nuevo Dato"></v-text-field>
    <v-btn @click="enviarDato">Enviar</v-btn>
      <ul>
        <li v-for="dato in datos" :key="dato.id">{{ dato.nombre }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        datos: []
      };
    },
    name: 'EjemPlo',
    mounted() {
      this.obtenerDatos();
    },
    methods: {
      obtenerDatos() {
        axios.get('http://localhost:5000/api/datos')
          .then(response => {
            this.datos = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      enviarDato() {
      axios.post('http://localhost:5000/api/datos', { nombre: this.nuevoDato })
        .then(response => {
          console.log(response.data);
          this.nuevoDato = ''; // Limpiar el campo de texto después de enviar el dato
          this.obtenerDatos(); // Volver a obtener los datos actualizados desde el backend
        })
        .catch(error => {
          console.error(error);
        });
       }
    }
  };
  </script>
  