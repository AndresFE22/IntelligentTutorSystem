<template>
  <div class="container">
    <background-animation />
    <v-container class="home-container" fluid fill-height>
      <v-layout align-center justify-center>
        <v-card class="home-card" elevation="10">
          <img src="../assets/pngwing.com.png" alt="">
          <v-card-text>
            <h1 class="display-1 line-spacing">
              Welcome to the Intelligent Tutor System!
            </h1>
          </v-card-text>
          <v-card-text>
            <h2 class="display-1">
              Topic: Climate Change
            </h2>
          </v-card-text>
          <v-card-text>
            <p class="subtitle-1 line-spacing">Let's develop your problem-solving skills related to climate change.</p>
          </v-card-text>
          <v-card-actions>
            <router-link to="/DiagnosisState">
              <v-btn :disabled="dialog" :loading="dialog" @click="dialog = true" color="#0084ff" large class="bt">
              <span class="mdi mdi-play-circle"></span> START
            </v-btn>
            </router-link>
          
          </v-card-actions>
        </v-card>
      </v-layout>
    </v-container>
<v-dialog
      v-model="dialog"
      :scrim="true"
      persistent
      width="auto"
    >
      <v-card
        color="primary"
      >
        <v-card-text>
          Please stand by
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
    
  </div>
</template>

<script>
import BackgroundAnimation from "./backgroundAnimation.vue";

export default {
  name: "HomeP",
  data () {
      return {
        dialog: false,
      }
    },
  components: {
    BackgroundAnimation,
  },
  watch: {
      dialog (val) {
        if (!val) return

        setTimeout(() => (this.dialog = false), 4000)
      },
    },  
  methods: {
    startActivity() {
    },
  },
};
</script>

<style scoped>

@media screen and (max-width: 900px) {
  img {
    width: 100px;

  }
  h1 {
    font-size: 20pt;
    margin-bottom: 25px;
  }

  h2 {
    font-size: 15pt;
    margin-bottom: 15px;
  }

  p {
    font-size: 12pt;
    margin-bottom: 15px;
  }
  .line-spacing {
  line-height: 1.2;
}
}

h1 {
  font-size: 30pt;
  font-weight: bold;
  font-family: 'Roboto', sans-serif;
  color: #0084ff;
  margin-bottom: 20px;
  }

  h2 {
  font-size: 20pt;
  font-weight: bold;
  font-family: 'Roboto', sans-serif;
  color: #727272;
  margin-bottom: 20px;

  }

p {
  font-size: 20pt;
  font-family: 'Roboto', sans-serif;
  margin-bottom: 20px;

}

img {
  width: 200px;
  margin-bottom: 20px;

}

.bt {
  font-family: 'Roboto', sans-serif;
  font-weight: bold;
  color: white;
}

.home-container {
  background-size: cover;
  background-position: center;
  display: grid;
  place-items: center;
  
}

.home-card {
  padding: 50px;
  text-align: center;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  width: 100%;
  margin-top: 50px;
  display: flex;
  align-items: center;
  flex-direction: column;;
}
</style>
