<template>
    <div class="container">
        <h1>ACTIVITIES</h1>
        <div class="slider-container">
            <div class="slider">
                <div v-if="additionalResources.length > 0" 
                    class="resource-card"
                    :style="resourceCardStyle">
                    <div class="resource-content">
                        <div class="resource-data">
                            <h2>{{ additionalResources[currentIndex][0].name }}</h2>
                            <p>Goal: {{ additionalResources[currentIndex][0].goal }}</p>
                            <p>Level: {{ additionalResources[currentIndex][0].lvl }}</p>
                            <p>PT: {{ additionalResources[currentIndex][0].pt }}</p>
                            <p>LC: {{ additionalResources[currentIndex][0].lc }}</p>
                        </div>
                        <div class="resource-media">
                            <div v-if="additionalResources[currentIndex][0].url === 't1Illustrationlow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url === 't1demonstrationlow'">
                                <video src="../../../../learning_resources/t1.mp4" controls autoplay></video>
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url === 't1objectivelow'">
                                <iframe src="../../../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1graphic_organizerlow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1additional_questionlow'">
                                <iframe src="../../../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1simulationslow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1questions_and_answerslow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1debatelow'">
                                <video src="../../../../learning_resources/t1.mp4"></video>
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1lecturelow'">
                                <iframe src="../../../../learning_resources/t1.txt" frameborder="0"></iframe>
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1microworldlow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1hypertextlow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1Analogie_and_relationshiplow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else-if="additionalResources[currentIndex][0].url == 't1experimentlow'">
                                <img src="../../../../learning_resources/t1.jpg" alt="imagen">
                            </div>
                            <div v-else>
                                <p>No se puede mostrar el recurso.</p>
                            </div>
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
            additionalResources: [],
            currentIndex: 0,
        };
    },
    computed: {
        resourceCardStyle() {
            return {
                width: '100%',
                display: this.additionalResources.length > 0 ? 'flex' : 'none'
            };
        }
    },

    mounted() {
        this.axiosCallSequential();
    },
    methods: {
        axiosCallSequential() {
            const id_student = this.$store.state.userId
            axios.get(`/api/Activity/${id_student}`) 
                .then(response => {
                    this.resources = response.data.resource_list;
                    this.additionalResources = response.data.resource_list_additional_2
                    console.log('additional', this.additionalResources)
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
        }
    }
};
</script>
  

<style>
.container {
    background-color: white;
    border-radius: 0 0 20px 20px;

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
    background-color: rgb(36, 149, 255);
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
    background-color: #0078c9;
    transform: scale(1.1);
}

.resource-data {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 10px;
    background-color: rgb(36, 149, 255);
    padding: 10px;
    border: 1px solid rgb(0, 132, 255);
    border-radius: 20px;
    color: white;
    font-weight: bold;
    place-items: center;

}

.resource-data h2,
.resource-data p {
    margin: 0;
}
</style>