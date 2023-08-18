<template>
  <div class="container">
    <h1>ACTIVITIES</h1>
    <div class="slider-container">
      <div class="slider">
        <div v-for="(resource, index) in resources" :key="index" class="resource-card" :class="{ 'active': index === currentIndex }">
          <div class="resource-content">
            <div class="resource-data">
              <h2>{{ resource.name }}</h2>
              <p>Goal: {{ resource.goal }}</p>
              <p>Level: {{ resource.lvl }}</p>
              <p>PT: {{ resource.pt }}</p>
              <p>LC: {{ resource.lc }}</p>
            </div>
            <div class="resource-media" v-if="resource.url.endsWith('.jpg')">
              <img :src="resource.url" alt="Imagen">
            </div>
            <div class="resource-media" v-else-if="resource.url.endsWith('.mp4')">
              <video controls>
                <source :src="resource.url" type="video/mp4">
                Tu navegador no admite el elemento de video.
              </video>
            </div>
            <div class="resource-media" v-else-if="resource.url.endsWith('.txt')">
              <iframe :src="resource.url"></iframe>
            </div>
            <div class="resource-media" v-else>
              <p>No se puede mostrar el recurso.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="buttons">
        <button class="prev-button" @click="prevSlide">Anterior</button>
        <button class="next-button" @click="nextSlide">Siguiente</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      resources: [],
      currentIndex: 0,
    };
  },
  mounted() {
    this.axiosCallSequential();
  },
  methods: {
    axiosCallSequential() {
      axios
        .get('/api/Activity')
        .then(response => {
          this.resources = response.data.data_global;
        })
        .catch(error => {
          console.log(error, 'Error al capturar');
        });
    },
    prevSlide() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    },
    nextSlide() {
      if (this.currentIndex < this.resources.length - 1) {
        this.currentIndex++;
      }
    },
  },
};
</script>

<style scoped>

.container { 
  background-image: url('../assets/fondoGlobal.jpg');
  background-size: cover;

}

.container h1 { 
  font-family: 'Roboto' sans-serif;
  font-weight: bold;
  color: #0099ff;
}
.slider-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.resource-card {
  display: none;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  border: 1px solid #ccc;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  
}

.resource-card.active {
  display: flex;
}

.resource-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.resource-media {
  margin-top: 20px;
}

.resource-media img,
.resource-media video,
.resource-media iframe {
  max-width: 100%;
  max-height: 70vh;
}

.buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 10px;
}

.prev-button,
.next-button {
  background-color: #0078c9;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  margin: 0 10px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.prev-button:hover,
.next-button:hover {
  background-color: #005a8c;
  transform: scale(1.1);
}
</style>
