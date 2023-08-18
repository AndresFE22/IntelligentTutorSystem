<template>
    <div class="container mt-4" id="container">
      <h1>Result LEARNING STYLES</h1>
      <table class="table table-bordered">
        <tr>
          <th></th>
          <th>5</th>
          <th>3</th>
          <th>1</th>
          <th>1</th>
          <th>3</th>
          <th>5</th>
          <th></th>
        </tr>
        <tr v-for="style in learningStyles" :key="style.name">
          <td>{{ style.name }}</td>
          <td v-for="subtraction in style.subtractions" :key="subtraction" :class="{ 'x-mark': isXMark(style, subtraction) }"></td>
          <td>{{ style.opposite }}</td>
        </tr>
      </table>
      <a href="/Activity">
        <button class="btn btn-primary" id="myButton">START ACTIVITIES</button>
      </a>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    mounted() {
      this.fetchData();
    },
    data() {
      return {
        learningStyles: [
        {
    name: 'ACTIVO',
    opposite: 'REFLEXIVO',
    subtractionsActivo: [5, 3, 1,],
    subtractionsReflexivo: [1, 3, 5]
  },
  {
    name: 'SENSORIAL',
    opposite: 'INTUITIVO',
    subtractions: [5, 3, 1, 1, 3, 5]
  },
  {
    name: 'VISUAL',
    opposite: 'VERBAL',
    subtractions: [5, 3, 1, 1, 3, 5]
  },
  {
    name: 'SECUENCIAL',
    opposite: 'GLOBAL',
    subtractions: [5, 3, 1, 1, 3, 5]
  }        ],
        results: [] // Aquí almacenaremos los resultados de la API
      };
    },
    methods: {
      fetchData() {
        axios.get('/api/StylesResults')
          .then(response => {
            this.results = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      isXMark(style, subtraction) {
        const result = this.results.find(result => result.dominant_style === style.dominant_style && result.subtraction === subtraction);
        return result ? true : false;
      }
    }
  };
  </script>
  
  <style scoped>
    .x-mark {
        background-color: rgb(0, 132, 255);
    }
</style>
  












