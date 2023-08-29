<template>
    <div class="background">
      <div class="container">
        <h1 class="mb-4">Test Learning Styles</h1>
        <br>
        <div v-if="!quizStarted">
          <h4>Ready! Now let's determine what your learning style is</h4>
          <br>
          <button class="btn btn-primary" @click="startQuiz">Start</button>
        </div>
        <div v-else>
          <div v-if="currentQuestion !== null" class="quiz-question">
            <h2>Question {{ currentQuestion + 1 }}</h2>
            <p class="question" style="font-family: 'Roboto' sans-serif; font-size: 17pt;">{{ questions[currentQuestion].question }}</p>
            <br>
            <select v-model="selectedAnswer" :name="'student_answer' + (currentQuestion + 1)" class="form-select mb-3" style="cursor: pointer;">
                <option v-for="(option, optionIndex) in questions[currentQuestion].options" :key="optionIndex" :value="option.value" :selected="optionIndex === 0">{{ option.text }}</option>
            </select>
            <br>
            <br>
            <v-btn class="btn-primary" color="#007bff" @click="nextQuestion" :disabled="selectedAnswer === ''">Next question <span class="mdi mdi-play"></span></v-btn>
            <router-link to="/">
              <button class="exit">Exit</button>
            </router-link>
          </div>
          <div v-else-if="showText">
            <h4>Quiz completed! Click the button below to submit your answers.</h4>
            <br>
            <br>
            <button class="btn btn-primary" @click="submitAnswers">Submit Answers</button>
          </div>
          <div v-if="ShowText_l">
            <h1 class="mb-4">Answers Submitted! <span class="mdi mdi-check-circle"></span></h1>
            <br>
          <h5>Your answers have been submitted. Thank you for completing the quiz!</h5>
          <br>
          <h3>Now we start with the activities</h3>
          <br>
            <router-link to="/ActivityITS">
              <button class="btn btn-primary">Submit Answers</button>
            </router-link>
          </div>
        </div>
        </div>
      </div>
  </template>

<style scoped>
.background {
  background-image: url('../assets/1110323_5592.jpg');
  background-size: 100% 100%;
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

h1 {
  color: #007bff;
  font-weight: bold;
  font-family: 'Roboto' sans-serif;
}

.question {
  font-family: 'Roboto' sans-serif;

}

.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 60px;
    background-color: white;
    border-radius: 20px;
    margin-bottom: 150px;
}

.quiz-question {
  margin-bottom: 40px;
}

.question {
  font-size: 18px;
  margin-bottom: 15px;
}

.form-select {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #e2e2e2;
  border-radius: 20px;
}

.btn-primary {
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  font-weight: bold;
  font-size: 12pt;
}

button {
    margin-left: 10px;
    
}

.exit {
    width: 70px;
    text-decoration: underline;
    font-size: 13pt;

}

</style>

  
  <script>

import axios from 'axios';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'; 
import { mapState } from 'vuex';

  export default {
    data() {
      return {
        quizStarted: false,
        showText: true,
        ShowText_l: false,
        questions: [
          {
            question: 'Entiendo mejor algo:',
            options: [
                { text: 'si lo practico.', value: 'a' },
                { text: 'si pienso en ello.', value: 'b' },
            
            ]
          },
          {
            question: ' Me considero:',
            options: [
              { text: 'Realista.', value: 'a' },
              { text: 'innovador.', value: 'b' },
             
            ]
          },

          {
            question: 'Cuando pienso acerca de lo que hice ayer, es más probable que lo haga sobre la base de:',
            options: [
              { text: 'una imagen.', value: 'a' },
              { text: 'palabras', value: 'b' },
          
            ]
          },

          {
            question: 'Tengo tendencia a:',
            options: [
              { text: 'entender los detalles de un tema pero no ver claramente su estructura completa.', value: 'a' },
              { text: 'entender la estructura completa pero no ver claramente los detalles.', value: 'b' },
             
            ]
          },

          {
    question: 'Cuando estoy aprendiendo algo nuevo, me ayuda:',
    options: [
      { text: 'hablar de ello.', value: 'a' },
      { text: 'pensar en ello.', value: 'b' },
    
    ]
  },
  {
    question: 'Si yo fuera profesor, yo preferiría dar un curso:',
    options: [
      { text: 'que trate sobre hechos y situaciones reales de la vida.', value: 'a' },
      { text: 'que trate con ideas y teorías.', value: 'b' },
    
    ]
  },
  {
    question: 'Prefiero obtener información nueva de:',
    options: [
      { text: 'imágenes, diagramas, gráficas o mapas.', value: 'a' },
      { text: 'instrucciones escritas o información verbal.', value: 'b' },
    
    ]
  },
  {
    question: 'Una vez que entiendo:',
    options: [
      { text: 'todas las partes, entiendo el total.', value: 'a' },
      { text: 'el total de algo, entiendo como encajan sus partes.', value: 'b' },
  
    ]
  },
  {
    question: 'En un grupo de estudio que trabaja con un material difícil, es más probable que:',
    options: [
      { text: 'participe y contribuya con ideas.', value: 'a' },
      { text: 'no participe y solo escuche.', value: 'b' },
     
    ]
  },
  {
    question: 'Es más fácil para mí:',
    options: [
      { text: 'aprender hechos.', value: 'a' },
      { text: 'aprender conceptos.', value: 'b' },
     
    ]
  },
  {
    question: 'En un libro con muchas imágenes y gráficas es más probable que:',
    options: [
      { text: 'revise cuidadosamente las imágenes y las gráficas.', value: 'a' },
      { text: 'me concentre en el texto escrito.', value: 'b' },
    
    ]
  },
  {
    question: 'Cuando resuelvo problemas de matemáticas:',
    options: [
      { text: 'generalmente trabajo sobre las soluciones con un paso a la vez.', value: 'a' },
      { text: 'frecuentemente sé cuales son las soluciones, pero luego tengo dificultad para imaginarme los pasos para llegar a ellas.', value: 'b' },
     
    ]
  },
  {
    question: 'En las clases a las que he asistido:',
    options: [
      { text: 'he llegado a saber como son muchos de los estudiantes.', value: 'a' },
      { text: 'raramente he llegado a saber como son muchos estudiantes.', value: 'b' },
      
    ]
  },
  {
    question: 'Cuando leo temas que no son de ficción, prefiero:',
    options: [
      { text: 'algo que me enseñe nuevos hechos o me diga como hacer algo.', value: 'a' },
      { text: 'algo que me dé nuevas ideas en que pensar.', value: 'b' },
     
    ]
  },
  {
    question: 'Me gustan los maestros:',
    options: [
      { text: 'que utilizan muchos esquemas en el pizarrón.', value: 'a' },
      { text: 'que toman mucho tiempo para explicar', value: 'b' },
 
    ]
  },

  {
    question: 'Cuando estoy analizando un cuento o una novela:',
    options: [
      { text: 'pienso en los incidentes y trato de acomodarlos para configurar los temas.', value: 'a' },
      { text: 'me doy cuenta de cuales son los temas cuando termino de leer y luego tengo que regresar y encontrar los incidentes que los demuestran.', value: 'b' },

    ]
  },
  {
    question: 'Cuando comienzo a resolver un problema de tarea, es más probable que:',
    options: [
      { text: 'comience a trabajar en su solución inmediatamente.', value: 'a' },
      { text: 'primero trate de entender completamente el problema.', value: 'b' },
    
    ]
  },
  {
    question: 'Prefiero la idea de:',
    options: [
      { text: 'certeza', value: 'a' },
      { text: 'teoría', value: 'b' },
    ]
  },
  {
    question: 'Recuerdo mejor:',
    options: [
      { text: 'lo que veo.', value: 'a' },
      { text: 'lo que oigo.', value: 'b' },
    ]
  },
  {
    question: 'Es más importante para mí que un profesor:',
    options: [
      { text: 'Exponga el material en pasos secuenciales claros.', value: 'a' },
      { text: 'me dé un panorama general y relacione el material con otros temas.', value: 'b' },
    ]
  },
        ],
        currentQuestion: 0,
        selectedAnswer: null,
        answers: []
      };
    },
    computed: {
  ...mapState(['auth'])
},
    methods: {
        startQuiz() {
      this.quizStarted = true;
      this.currentQuestion = 0;
      },
        nextQuestion() {
        this.answers.push(this.selectedAnswer);
        if (this.currentQuestion < this.questions.length - 1) {
          this.currentQuestion++;
          this.selectedAnswer = null;
        } else {
          this.currentQuestion = null;
        }
      },
        submitAnswers() {
            axios.post('/api/test', { answers : this.answers})
            .then(response => {
                console.log(response.data);
                this.showText = false;
                this.ShowText_l = true;
            })
            .catch(error => {
                console.log(error, 'Error al enviar')
            }) 
        }

    }
  };
  </script>
  
  