<template>
    <div class="container">
      <div class="background-image"></div> 
      <ul class="nav nav-tabs menu-tabs">
        <li v-if="nav_menu === 'Secuencial'" class="nav-item">
          <a class="nav-link" :class="{ 'active': activeTab === 'sequentialTab' }" @click="changeTab('sequentialTab')">Secuencial</a>
        </li>
        <li v-else-if="nav_menu === 'Global'" class="nav-item">
          <a class="nav-link" :class="{ 'active': activeTab === 'globalTab' }" @click="changeTab('globalTab')">Global</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" :class="{ 'active': activeTab === 'evaluationTab' }" @click="changeTab('evaluationTab')">Evaluación</a>
        </li>
      </ul>
      <div id="ActivitySequential" v-show="activeTab === 'sequentialTab'">
        <ResourcesViewsSequential v-if="activeTab === 'sequentialTab'" />
      </div>
      <div id="ActivityGlobal" v-show="activeTab === 'globalTab'">
        <ResourcesViewsGlobal v-if="activeTab === 'globalTab'" />
      </div>
      <div id="diagnosisStateEvaluation" v-show="activeTab === 'evaluationTab'">
        <diagnosis-state-evaluation v-if="activeTab === 'evaluationTab'" />
      </div>
    </div>
  </template>
  
  <script>
  
  import ResourcesViewsGlobal from './ResourcesViewGlobal.vue';
  import ResourcesViewsSequential from './ResourcesViewSequential.vue';
  import DiagnosisStateEvaluation from './diagnosisStateEvaluation.vue';
  import axios from 'axios';
  
  export default {
    components: {
      ResourcesViewsGlobal,
      ResourcesViewsSequential,
      DiagnosisStateEvaluation,
    },
    data() {
      return {
        nav_menu: '', 
        activeTab: '', 
      };
    },
    mounted() {
      axios.get('/api/Activity') 
        .then(response => {
          this.nav_menu = response.data.nav_menu; 
          this.activeTab = this.nav_menu === 'Secuencial' ? 'sequentialTab' : this.nav_menu === 'Global' ? 'globalTab' : 'evaluationTab';
        })
        .catch(error => {
          console.error(error);
        });
    },
    methods: {
      changeTab(tab) {
        this.activeTab = tab;
      },
    },
  };
  </script>
  
  <style scoped>
  .menu-tabs {
    margin-top: 20px;
  }
  .menu-tabs .nav-item {
    cursor: pointer;
  }
  .menu-tabs .nav-link.active {
    font-weight: bold;
  }

  .background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("../assets/fondoGlobal.jpg");
  background-size: cover;
  z-index: -1; 
   
}


  </style>
  