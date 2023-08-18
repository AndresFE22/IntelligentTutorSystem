<template>
    <div class="template" >
    <div class="resources-container">
      <div class="resource-center">
        <div class="resource-card" v-for="(resource, index) in resources" :key="index" :class="{ 'active': index === currentIndex }">
          <div class="resource-data">
            <h2>{{ resource.name }}</h2>
            <p>Goal: {{ resource.goal }}</p>
            <p>Level: {{ resource.lvl }}</p>
            <p>PT: {{ resource.pt }}</p>
            <p>LC: {{ resource.lc }}</p>
          </div>
          <div v-if="resource.url.endsWith('.jpg')" class="resource-media">
            <img :src="resource.url" alt="Imagen">
          </div>
          <div v-else-if="resource.url.endsWith('.mp4')" class="resource-media">
            <video controls>
              <source :src="resource.url" type="video/mp4">
              Tu navegador no admite el elemento de video.
            </video>
          </div>
          <div v-else-if="resource.url.endsWith('.txt')" class="resource-media">
            <iframe :src="resource.url"></iframe>
          </div>
          <div v-else class="resource-media">
            <p>No se puede mostrar el recurso.</p>
          </div>
        </div>
      </div>
      <div class="buttons">
    <div class="button-container" ref="buttonContainer">
      <div class="button-slider" ref="buttonSlider" @mousedown="startDrag" @mousemove="handleDrag" @mouseup="endDrag" @mouseleave="endDrag">
        <button v-for="(resource, index) in resources" :key="index" class="custom-resource-button" @click="changeSlide(index)" :style="getButtonStyle(index)">
          {{ index + 1 }}
        </button>
      </div>
    </div>
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
        isDragging: false,
        startX: 0,
        offsetX: 0,
      };
    },
    mounted() {
      this.axiosCallGlobal();
      this.initButtonSlider();
    },


    methods: {
      axiosCallGlobal() {
        axios.get('/api/Activity')
          .then(response => {
            this.resources = response.data.data_sequential;
          })
          .catch(error => {
            console.log(error, 'Error al capturar');
          });
      },
      changeSlide(index) {
        this.currentIndex = index;
      },

      initButtonSlider() {
      let buttonSlider = this.$refs.buttonSlider;
      let buttons = buttonSlider.querySelectorAll('.custom-resource-button');
      let buttonWidth = buttons[0].offsetWidth;
      buttonSlider.style.width = `${buttonWidth * buttons.length}px`;
    },

    startDrag(event) {
      this.isDragging = true;
      this.startX = event.clientX - this.offsetX;
    },
    handleDrag(event) {
      if (!this.isDragging) return;
      this.offsetX = event.clientX - this.startX;
      this.clampOffset();
    },
    endDrag() {
      this.isDragging = false;
      this.clampOffset();
    },
    clampOffset() {
      let buttonSlider = this.$refs.buttonSlider;
      let minOffset = -(buttonSlider.offsetWidth - window.innerWidth);
      let maxOffset = 0;
      this.offsetX = Math.min(maxOffset, Math.max(minOffset, this.offsetX));
    },
    getButtonStyle() {
      let transform = `translateX(${this.offsetX}px)`;
      return {
        transform,
        transition: this.isDragging ? 'none' : 'transform 0.3s ease',
      };
    },
  },
};

  </script>
  
  <style scoped>
.resources-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-image: url('../assets/fondoGlobal.jpg');
  background-size: cover;
  padding: 50px;
}

.resource-center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.resource-card {
  display: none;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  height: 100%;
  border: 1px solid #ccc;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}

.resource-card.active {
  display: flex;
}

.resource-media img,
.resource-media video,
.resource-media iframe {
  max-width: 100%;
  max-height: 100%;
}

.buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 10px;
  width: 100%; 
  height: 100px;
  position: relative;
  background-color: #f1f1f1;
  overflow: hidden;
  border-radius: 20px;
}

.button-container {
  display: flex;
  align-items: center;
  overflow: hidden;
  width: 100%; /* Ancho del contenedor de botones */
}

.button-slider {
  position: absolute;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  overflow: hidden;
  transition: transform 0.3s ease;
}


.custom-resource-button {
  width: 40px;
  height: 40px;
  margin: 0 10px;
  font-size: 18px;
  background-color: #3498db;    
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.custom-resource-button:hover {
  background-color: #0078c9;
  transform: scale(1.1);
}

.active-button {
  background-color: #0078c9;
}

  </style>
  