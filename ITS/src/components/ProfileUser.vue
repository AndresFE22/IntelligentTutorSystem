<template>
  <div class="profile">
    <h2>my profile</h2>
    <div class="profile-info">
      <div class="imgbox">
        <div class="circle">
          <img v-if="user.picture" :src="getImageUrl(user.picture, user.format)" :alt="user.user" class="imagen">
        </div>
      </div>
      <div class="conItem">
        <div class="item">
        <p><strong>ID:</strong> {{ user.Id }} </p>
      </div>
      <div class="item">
        <p><strong>Name:</strong> {{ user.name }} </p>
      </div>
      <div class="item">
        <p><strong>User:</strong> {{ user.users }} </p>
      </div>
      <div class="item">
        <p><strong>Learning Style:</strong> {{ user.Ls }} </p>
      </div>
      <div class="change">
        <input v-b-modal.modal-center type="button" class="toggle-button" value="change password"/>
      </div>
      </div>
    </div>
    <b-modal id="modal-center" centered title="Change password">
    <div class="containModal">
      <v-text-field v-model="currentPassword" label="Enter your current password"></v-text-field>
      <v-text-field v-model="newPassword" label="Enter your new password"></v-text-field>
      <br>
      <center><v-btn @click="changePassword">Change password</v-btn></center>
      <br>
      <div v-if="message" class="message">{{ message }}</div>
    </div>
  </b-modal>
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
      currentPassword: '',
      newPassword : '',
      message: ''
      
    };
  },
  // async mounted() {
  //   try {
  //     const response = await axios.get(`/api/dataUser/${this.userId}`);
  //     this.user = response.data;
  //   } catch (error) {
  //     console.error(error);
  //   }
  // },
  methods: {
    getImageUrl(imagenBase64, format) {
      return `data:image/${format};base64,${imagenBase64}`;
    },
    changePassword(){
    const formData = new FormData()
    formData.append('id', this.userId)
    formData.append('currentPassword', this.currentPassword)
    formData.append('newPassword', this.newPassword)
    axios
    .put('/api/changePassword', formData)
    .then(response => {
      this.message = response.data.message
      setTimeout(() => {
            this.mensaje = "";
          }, 3000)
      this.currentPassword = '',
      this.newPassword = ''
    })
    .catch(error =>  {
      console.error(error)
    })
  }
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

.mensaje {
  background-color: green;
  color: white;
  padding: 10px;
  border-radius: 20px;
}

.profile-info {
  margin-top: 20px;
  text-align: left;
}

.hidden-content {
  color: #999;
  font-style: italic;
}

.item {
  display: flex;
  align-items: center;
  background-color: rgba(241, 241, 241, 0.705);
  padding: 8px;
  margin-bottom: 10px;
  margin-top: 10px;
  border-radius: 15px;
}

.change {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  margin-bottom: 10px;
  margin-top: 10px;
  color: rgb(0, 162, 255);
}


.toggle-button{
 text-decoration: underline;
} 

strong {
  color: rgb(0, 162, 255);

}
</style>
