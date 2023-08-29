<template>
  <div class="profile">
    <h2>Mi Perfil</h2>
    <div class="profile-info">
      <img v-if="user.picture" :src="getImageUrl(user.picture, user.format)" :alt="palabra.palabra" class="imagen">
      <p><strong>ID:</strong> {{ user.Id }}</p>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>User:</strong> {{ user.users }}</p>
      <p><strong>Password:</strong> {{ user.password }}</p>
      <p><strong>Learning Style:</strong> {{ user.Ls }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['auth']),
    userId() {
      return this.$store.state.userId
    }
  },
  data() {
    return {
      user: []
    };
  },
  async mounted() {
    try {
      const response = await axios.get(`/api/dataUser/${this.userId}`);
      this.user = response.data
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    getImageUrl(imagenBase64, format) {
      return `data:image/${format};base64,${imagenBase64}`;
    }
  }
}
</script>

<style scoped>
</style>
