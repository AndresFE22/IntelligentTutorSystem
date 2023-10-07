<template>
  <div class="container">
  <h1>ACTIVITIES</h1>
    <div class="resources-container">
      <div class="resource-center">
        <div v-if="resources.length > 0" class="resource-card" :style="resourceCardStyle">
          <div class="resource-content">
            <div v-if="currentIndex < resources.length" class="resource-data">
              <h2>{{ resources[currentIndex].name }}</h2>
              <p>Goal: {{ resources[currentIndex].goal }}</p>
              <p>Level: {{ resources[currentIndex].lvl }}</p>
              <p>PT: {{ resources[currentIndex].pt }}</p>
              <p>LC: {{ resources[currentIndex].lc }}</p>
            </div>
            <div class="resource-media">
              <div v-if="resources[currentIndex].url === 't1Illustrationlow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else-if="resources[currentIndex].url === 't1demonstrationlow'">
                <video src="../../learning_resources/t1.mp4" controls autoplay></video>
              </div>
              <div v-else-if="resources[currentIndex].url === 't1objectivelow'">
                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
              </div>
              <div v-else-if="resources[currentIndex].url == 't1graphic_organizerlow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else-if="resources[currentIndex].url == 't1additional_questionlow'">
                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
              </div>
              <div v-else-if="resources[currentIndex].url == 't1simulationslow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else-if="resources[currentIndex].url == 't1questions_and_answerslow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else-if="resources[currentIndex].url == 't1debatelow'">
                <video src="../../learning_resources/t1.mp4"></video>
              </div>
              <div v-else-if="resources[currentIndex].url == 't1lecturelow'">
                <iframe src="../../learning_resources/t1.txt" frameborder="0"></iframe>
              </div>
              <div v-else-if="resources[currentIndex].url == 't1microworldlow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else-if="resources[currentIndex].url == 't1hypertextlow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else-if="resources[currentIndex].url == 't1Analogie_and_relationshiplow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else-if="resources[currentIndex].url == 't1experimentlow'">
                <img src="../../learning_resources/t1.jpg" alt="imagen">
              </div>
              <div v-else>
                <p>No se puede mostrar el recurso.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="buttons">
        <div class="button-container" ref="buttonContainer">
          <div class="button-slider" ref="buttonSlider" @mousedown="startDrag" @mousemove="handleDrag" @mouseup="endDrag"
            @mouseleave="endDrag">
            <button v-for="(resource, index) in resources" :key="index" class="custom-resource-button"
              @click="changeSlide(index)" :style="getButtonStyle(index)">
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
      additionalResources: [],
      currentIndex: 0,
      isDragging: false,
      startX: 0,
      offsetX: 0,
    };
  },
  computed: {
    resourceCardStyle() {
      return {
        width: '100%',
        display: this.resources.length > 0 ? 'flex' : 'none'
      };
    }
  },
  mounted() {
    this.axiosCallGlobal();
    window.addEventListener('load', this.initButtonSlider);
  },
  beforeDestroy() {
  window.removeEventListener('load', this.initButtonSlider);
},
  methods: {
    axiosCallGlobal() {
      const id_student = this.$store.state.userId
      axios.get(`/api/Activity/${id_student}`) 
        .then(response => {
          this.resources = response.data.resource_list;
          this.additionalResources_1 = response.data.resource_list_additional_1
          this.additionalResources_2 = response.data.resource_list_additional_2

          
        })
        .catch(error => {
          console.log(error, 'Error al capturar');
        });
    },
    changeSlide(index) {
      if (index >= 0 && index < this.resources.length) {
        this.currentIndex = index;
      }
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
    getButtonStyle(index) {
      let transform = `translateX(${this.offsetX}px)`;
      return {
        transform,
        transition: this.isDragging ? 'none' : 'transform 0.3s ease',
        visibility: index < this.resources.length ? 'visible' : 'hidden',
      };
    },
  },
};
</script>

  
<style scoped>

.container { 
  background-color: white;
  border-radius: 0 0 20px 20px;

}

.container h1 { 
  font-family: 'Roboto' sans-serif;
  font-weight: bold;
  color: #0099ff;
}

.resources-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;   
}

.resource-center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.resource-card {
  display: none;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  border-radius: 20px 20px 0 0;
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
  width: 100%;
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
  