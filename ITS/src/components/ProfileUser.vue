<template>
  <div class="profile">
    <h2>Mi Perfil</h2>
    <div class="profile-info">
      <div class="imgbox">
        <div class="circle">
          <img v-if="user.picture" :src="getImageUrl(user.picture, user.format)" :alt="user.user" class="imagen">
        </div>
      </div>
      <p><strong>ID:</strong> {{ user.Id }}</p>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>User:</strong> {{ user.users }}</p>
      <p><strong>Password:</strong> {{ hiddenPassword }}</p>
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
      return this.$store.state.userId;
    },
    hiddenPassword() {
      return '*'.repeat(this.user.password.length)
    }
  },
  data() {
    return {
      user: {},
    };
  },
  async mounted() {
    try {
      const response = await axios.get(`/api/dataUser/${this.userId}`);
      this.user = response.data;
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    getImageUrl(imagenBase64, format) {
      return `data:image/${format};base64,${imagenBase64}`;
    },
  },
};
</script>

<style scoped>
.profile {
  text-align: center;
}

.imgbox {
  width: 150px;
  height: 150px;
  margin: 0 auto;
  position: relative;
}

.circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.imagen {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-info {
  margin-top: 20px;
  text-align: left;
}

.hidden-content {
  color: #999;
  font-style: italic;
}
</style>
