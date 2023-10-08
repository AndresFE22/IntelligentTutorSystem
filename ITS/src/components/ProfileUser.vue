<template>
  <div class="profile">
    <table class="profile-table">
      <tr>
        <td class="profile-picture-cell" rowspan="4">
          <img :src="user.picture" alt="Foto de perfil" class="round-image" />
        </td>
        <td  class="title">Nombre Completo:</td>
        <td>{{ user.name }}</td>
      </tr>
      <tr>
        <td  class="title">ID de Usuario:</td>
        <td>{{ user.Id }}</td>
      </tr>
      <tr>
        <td  class="title">Nombre de Usuario:</td>
        <td>{{ user.users }}</td>
      </tr>
      <tr>
        <td class="title">Estilo de aprendizaje:</td>
        <td>{{ user.Ls }}</td>
      </tr>
    </table>

    <!-- Botones para abrir modales -->
    <div class="button-container">
      <b-button @click="openModal('TestTopic')">Abrir Test Topic</b-button>
      <b-button @click="openModal('TestStyle')">Abrir Test Style</b-button>
    </div>

    <!-- Modales -->
    <b-modal v-if="modalType === 'TestTopic'" title="Test Topic">
      Contenido del modal para Test Topic
    </b-modal>
    <b-modal v-if="modalType === 'TestStyle'" title="Test Style">
      Contenido del modal para Test Style
    </b-modal>
  </div>
</template>
<script>

import axios from 'axios';

export default {
  data() {
    return {
      user: {},
      modalType: null
    };
  },

  mounted() {
    this.dataUser()
  },

  methods: {
    async dataUser() {
      const id_student = this.$store.state.userId
    try {
      const response = await axios.get(`/api/dataUser/${id_student}`);
      this.user = response.data;
      console.log(this.user)
    } catch (error) {
      console.error(error);
    }
    },
    openModal(type) {
      this.modalType = type;
    }
  }
};
</script>

<style scoped>
.profile {
  display: flex;
  justify-content: center;
  align-items: center;
}

.title {
 font-weight: bold;
 background-color: rgb(223, 223, 223);
}
.profile-table {
  border-collapse: collapse;
  width: 80%;
  margin: 20px;
}

.profile-table td {
  padding: 8px;
  border: 1px solid #ccc;
}


.profile-picture-cell {
  width: 300px; /* Ajusta el ancho de la celda de la imagen según tus preferencias */
}

.profile-picture {
  margin-bottom: 1rem;
}

.round-image {
  width: 100%;
}

.profile-info {
  margin-bottom: 1rem;
}

.button-container {
  display: flex;
  justify-content: center;
}

.b-button {
  margin: 0 0.5rem;
}
</style>
