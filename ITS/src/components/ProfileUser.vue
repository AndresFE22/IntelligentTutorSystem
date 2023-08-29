<template>
    <div class="profile">
      <h2>Mi Perfil</h2>
      <div class="profile-info">
        <p><strong>Name:</strong> {{ user.name }}</p>
        <p><strong>User:</strong> {{ user.user }}</p>
        <p><strong>Learning Styles:</strong> {{ user.Learning_styles }}</p>
      </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';

  export default {
    data() { 
      return {
        user: {}
      }
    }, 
    methods: {
      dataUser() {
        axios.get('api/dataUser')
        .then(response => {
          console.log(response.data)
          this.user = response.data
        } )
        .catch(error => {
          console.log('error al capturar', error)
        })
      }
    }
  }
  </script>
  
  <style scoped>
  </style>
  