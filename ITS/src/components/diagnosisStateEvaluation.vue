<template>
  <div class="background">
    <div class="container">
      <h1 v-if="showTitle" class="mb-4">Climate Change Quiz</h1>
      <br>
      <div v-if="!quizStarted">
        <h4>Welcome! Get ready to answer some questions about climate change.</h4>
        <br>
        <button class="btn btn-primary" @click="startQuiz">Start</button>
      </div>
      <div v-else>
        <div v-if="visibleQuestionsIndex !== null && visibleQuestionsIndex < hiddenQuestions.length" class="quiz-question">
        <h2>Question {{ currentVisibleQuestion }}</h2>
        <p class="question" style="font-family: 'Roboto' sans-serif; font-size: 17pt;">{{ questions[hiddenQuestions[visibleQuestionsIndex] - 1].question }}</p>
        <br>
        <select v-model="selectedAnswer" :name="'student_answer' + (hiddenQuestions[visibleQuestionsIndex])" class="form-select mb-3" style="cursor: pointer;">
        <option v-for="(option, optionIndex) in questions[hiddenQuestions[visibleQuestionsIndex] - 1].options" :key="optionIndex" :value="option.value" :selected="optionIndex === 0">{{ option.text }}</option>
        </select>
  <br>
  <br>
  <v-btn class="btn-primary" color="#007bff" @click="nextQuestion" :disabled="selectedAnswer == ''">Next question <span class="mdi mdi-play"></span></v-btn>
  <router-link to="/">
    <button class="exit">Exit</button>
  </router-link>
</div>

        <div v-else-if="showMessage">
          <h4>You have finished the quiz on the topic. now send your answers</h4>
          <br>
          <button class="btn btn-primary" @click="submitAnswers">Submit</button>
        </div>
        <div v-if="showSubmitMessage">
      <div class="submit-message">
          <h1 class="mb-4">Answers Submitted! <span class="mdi mdi-check-circle"></span></h1>
          <br>
        <h5>Your answers have been submitted. Thank you for completing the quiz!</h5>
        <br>
        <h3>Let's determine your learning style, press continue</h3>
        <br>
        <router-link to="/DiagnosisStyles">
          <button class="btn btn-primary">Continue</button>
        </router-link> 
      </div>
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

export default {
  data() {
    return {
      id_student: null,
      showSubmitMessage: false,
      showMessage: true,
      quizStarted: false,
      showTitle: true,
      visibleQuestionsIndex: null,
      currentVisibleQuestion: 0,
      questions: [
        {
          id: 1,
          question: 'Which gas is known as the "silent killer" because of its role in trapping heat in the atmosphere?',
          options: [
              { text: 'Oxygen (O2)', value: 'a' },
              { text: 'Nitrogen (N2)', value: 'b' },
              { text: 'Carbon dioxide (CO2)', value: 'c' },
              { text: 'Methane (CH4)', value: 'd' }
          ]
        },
        {
          id: 2,
          question: 'What is deforestation?',
          options: [
            { text: 'The process of planting trees', value: 'a' },
            { text: 'The conversion of forests into urban areas', value: 'b' },
            { text: 'The removal of trees and forests', value: 'c' },
            { text: 'The practice of recycling paper', value: 'd' }
          ]
        },

        {
          id: 3,
          question: 'What is a major source of greenhouse gas emissions from human activities?',
          options: [
            { text: 'Volcanic eruptions', value: 'a' },
            { text: 'Burning fossil fuels', value: 'b' },
            { text: 'Natural soil processes', value: 'c' },
            { text: 'Deforestation', value: 'd' }
          ]
        },

        {          
          id: 4,
          question: 'What is a simple way to conserve energy in your home?',
          options: [
            { text: 'Leaving lights on when not needed', value: 'a' },
            { text: 'Turning off electronics when not in use', value: 'b' },
            { text: 'Opening windows during cold weather(CO2)', value: 'c' },
            { text: 'Using a space heater in every room', value: 'd' }
          ]
        },

        {
        id: 5,
  question: 'What does "energy efficiency" mean?',
  options: [
    { text: 'Using more energy than necessary', value: 'a' },
    { text: 'Using energy without consideration for the environment', value: 'b' },
    { text: 'Using less energy to accomplish the same tasks', value: 'c' },
    { text: 'Using only renewable energy sources', value: 'd' }
  ]
},
{
  id: 6,
  question: 'What is a benefit of using energy-efficient appliances?',
  options: [
    { text: 'Higher energy consumption', value: 'a' },
    { text: 'Lower electricity bills', value: 'b' },
    { text: 'Increased greenhouse gas emissions', value: 'c' },
    { text: 'Greater dependence on fossil fuels', value: 'd' }
  ]
},
{
  id: 7,
  question: 'What is a common source of marine plastic pollution?',
  options: [
    { text: 'Volcanic eruptions', value: 'a' },
    { text: 'Medical waste', value: 'b' },
    { text: 'Sewage', value: 'c' },
    { text: 'Radioactive waste', value: 'd' }
  ]
},
{
  id: 8,
  question: 'What is one way to reduce plastic waste in your daily life?',
  options: [
    { text: 'Using disposable plastic bags', value: 'a' },
    { text: 'Buying bottled water', value: 'b' },
    { text: 'Using a reusable water bottle', value: 'c' },
    { text: 'Throwing plastic waste in the ocean', value: 'd' }
  ]
},
{
  id: 9,
  question: 'What are microplastics?',
  options: [
    { text: 'Large pieces of plastic waste found in oceans', value: 'a' },
    { text: 'Plastic waste that cannot be recycled', value: 'b' },
    { text: 'Tiny plastic particles that pollute the environment', value: 'c' },
    { text: 'Biodegradable plastics', value: 'd' }
  ]
},
{
  id: 10,
  question: 'What is the primary greenhouse gas responsible for trapping heat in the Earth\'s atmosphere?',
  options: [
    { text: 'Carbon dioxide (CO2)', value: 'a' },
    { text: 'Methane (CH4)', value: 'b' },
    { text: 'Nitrous oxide (N2O)', value: 'c' },
    { text: 'Water vapor (H2O)', value: 'd' }
  ]
},
{          
  id: 11,
  question: 'Deforestation refers to the process of:',
  options: [
    { text: 'Increasing forest coverage', value: 'a' },
    { text: 'Planting more trees', value: 'b' },
    { text: 'Clearing or removing trees from an area', value: 'c' },
    { text: 'Building structures within forests', value: 'd' }
  ]
},
{
  id: 12,
  question: 'Which of the following human activities contributes significantly to greenhouse gas emissions?',
  options: [
    { text: 'Walking and biking', value: 'a' },
    { text: 'Using energy-efficient appliances', value: 'b' },
    { text: 'Burning fossil fuels for transportation', value: 'c' },
    { text: 'Recycling paper and plastic', value: 'd' }
  ]
},
{
  id: 13,
  question: 'Which of the following is an effective way to conserve energy at home?',
  options: [
    { text: 'Leaving lights and electronics on when not in use', value: 'a' },
    { text: 'Setting the thermostat to a very high temperature', value: 'b' },
    { text: 'Using energy-efficient appliances and light bulbs', value: 'c' },
    { text: 'Opening windows and doors during cold weather', value: 'd' }
  ]
},
{
  id: 14,
  question: 'What is the purpose of an energy audit?',
  options: [
    { text: 'To increase energy consumption', value: 'a' },
    { text: 'To identify ways to reduce energy usage', value: 'b' },
    { text: 'To promote the use of fossil fuels', value: 'c' },
    { text: 'To encourage deforestation', value: 'd' }
  ]
},
{
  id: 15,
  question: 'Which of the following is a renewable source of energy?',
  options: [
    { text: 'Natural gas', value: 'a' },
    { text: 'Coal', value: 'b' },
    { text: 'Wind power', value: 'c' },
    { text: 'Nuclear power', value: 'd' }
  ]
},

{
  id: 16,
  question: 'Which of the following is a common single-use plastic item that contributes to pollution?',
  options: [
    { text: 'Reusable water bottle', value: 'a' },
    { text: 'Paper bag', value: 'b' },
    { text: 'Plastic straw', value: 'c' },
    { text: 'Glass container', value: 'd' }
  ]
},
{
  id: 17,
  question: 'Which of the following actions can help reduce plastic waste?',
  options: [
    { text: 'Using single-use plastic items', value: 'a' },
    { text: 'Recycling plastic waste', value: 'b' },
    { text: 'Throwing plastic waste in rivers', value: 'c' },
    { text: 'Ignoring plastic waste', value: 'd' }
  ]
},
{
  id: 18,
  question: 'What are microplastics?',
  options: [
    { text: 'Large pieces of plastic waste found in oceans', value: 'a' },
    { text: 'Plastic waste that cannot be recycled', value: 'b' },
    { text: 'Tiny plastic particles that pollute the environment', value: 'c' },
    { text: 'Biodegradable plastics', value: 'd' }
  ]
},
{
  id: 19,
  question: 'Which of the following is a major greenhouse gas responsible for global warming?',
  options: [
    { text: 'Carbon dioxide (CO2)', value: 'a' },
    { text: 'Nitrogen (N2)', value: 'b' },
    { text: 'Oxygen (O2)', value: 'c' },
    { text: 'Water vapor (H2O)', value: 'd' }
  ]
},
{
  id: 20,
  question: 'Which human activity is a major cause of deforestation?',
  options: [
    { text: 'Mining', value: 'a' },
    { text: 'Fishing', value: 'b' },
    { text: 'Agriculture', value: 'c' },
    { text: 'Air travel', value: 'd' }
  ]
},
{
  id: 21,
  question: 'Which industry is a significant contributor to greenhouse gas emissions?',
  options: [
    { text: 'Fashion industry', value: 'a' },
    { text: 'Renewable energy industry', value: 'b' },
    { text: 'Entertainment industry', value: 'c' },
    { text: 'Education industry', value: 'd' }
  ]
},
{
  id: 22,
  question: 'Which of the following is an example of energy-efficient lighting?',
  options: [
    { text: 'Incandescent light bulb', value: 'a' },
    { text: 'Compact fluorescent lamp (CFL)', value: 'b' },
    { text: 'Halogen lamp', value: 'c' },
    { text: 'Neon light', value: 'd' }
  ]
},

{
  id: 23,
  question: 'What can you do to reduce energy consumption in your home?',
  options: [
    { text: 'Keep lights and appliances on when not in use', value: 'a' },
    { text: 'Set the thermostat to a high temperature in winter', value: 'b' },
    { text: 'Use energy-efficient appliances', value: 'c' },
    { text: 'Keep windows and doors open during hot days', value: 'd' }
  ]
},
{
  id: 24,
  question: 'Which of the following is a renewable source of energy?',
  options: [
    { text: 'Natural gas', value: 'a' },
    { text: 'Coal', value: 'b' },
    { text: 'Petroleum', value: 'c' },
    { text: 'Solar power', value: 'd' }
  ]
},
{
  id: 25,
  question: 'Which of the following actions can help reduce plastic waste?',
  options: [
    { text: 'Using single-use plastic items', value: 'a' },
    { text: 'Recycling plastic waste', value: 'b' },
    { text: 'Throwing plastic waste in rivers', value: 'c' },
    { text: 'Ignoring plastic waste', value: 'd' }
  ]
},
{
  id: 26,
  question: 'Which of the following is a commonly used plastic that contributes to pollution?',
  options: [
      { text: 'Polyethylene (PE)', value: 'a' },
      { text: 'Gold', value: 'b' },
      { text: 'Wood', value: 'c' },
      { text: 'Glass', value: 'd' }
      ]
  },
  {
    id: 27,
  question: 'Which of the following is a primary source of marine plastic pollution?',
  options: [
      { text: 'Volcanic eruptions', value: 'a' },
      { text: 'Medical waste', value: 'b' },
      { text: 'Sewage', value: 'c' },
      { text: 'Radioactive waste', value: 'd' }
      ]
  }
      ],
      currentQuestion: 0,
      selectedAnswer: null,
      answers: []
    };

  },
  mounted() {
    this.axiosCallEvaluation(); 
    },

    computed: {
    visibleQuestions() {
      return this.questions.filter(question => this.hiddenQuestions.includes(question.id));
    },
  },

  methods: {
      startQuiz() {
    this.quizStarted = true;
    this.visibleQuestionsIndex = this.hiddenQuestions.findIndex(id => id === 1);
    },

    axiosCallEvaluation(){
      const id_student = this.$store.state.userId
            axios
            .get(`/api/Activity/${id_student}`)
            .then(response => {
                this.hiddenQuestions  = response.data.data_incorrect_answer
                console.log(response.data.data_incorrect_answer)
                console.log("hidden", this.hiddenQuestions)
                this.currentVisibleQuestion = this.hiddenQuestions[0]; 

            })
            .catch(error => {
                console.log(error, 'error al capturar respuestas incorrectas')
            })},
          
            nextQuestion() {
      this.answers.push(this.selectedAnswer);
      const nextIndex = this.visibleQuestionsIndex + 1;
      if (nextIndex < this.hiddenQuestions.length) {
        this.visibleQuestionsIndex = nextIndex;
        this.currentVisibleQuestion++
        this.selectedAnswer = null;
      } else {
        this.visibleQuestionsIndex = null;
      }
    },
         submitAnswers() {
          const id_student = this.$store.state.userId
          axios.post(`/api/diagnosisEvaluation/${id_student}`, { answers : this.answers})
          .then(response => {
              console.log(response.data);
              this.showSubmitMessage = true;
              this.showMessage = false
              this.showTitle = false;
          })
          .catch(error => {
              console.log(error, 'Error al enviar')
          }) 
      }

  }
};
</script>











