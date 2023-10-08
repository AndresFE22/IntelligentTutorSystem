<template>
    <div class="container">
      <div class="background-image"></div> 
      <ul class="nav nav-tabs menu-tabs">
        <b-dropdown id="dropdown-left" text="Activities" variant="primary" class="m-2" v-if="nav_menu === 'Secuencial'">
        <b-dropdown-item>
          <a class="nav-link" :class="{ 'active': activeTab === 'sequentialTab' }" @click="changeTab('sequentialTab')">Activity</a>
        </b-dropdown-item>
        <b-dropdown-item v-if="nav_menu == 'Secuencial' && Object.keys(additionalResource_1).length > 0">
          <a class="nav-link" :class="{ 'active': activeTab === 'RAS_1'  }" @click="changeTab('RAS_1')" >Activity1</a>
        </b-dropdown-item>
        <b-dropdown-item v-if="nav_menu == 'Secuencial' && Object.keys(additionalResource_2).length > 0">
          <a class="nav-link" :class="{ 'active': activeTab === 'RAS_2'  }" @click="changeTab('RAS_2')" >Activity2</a>        
        </b-dropdown-item>
    </b-dropdown>

    <b-dropdown id="dropdown-left" text="Activities" variant="primary" class="m-2" v-if="nav_menu === 'Global'">
        <b-dropdown-item>
          <a class="nav-link" :class="{ 'active': activeTab === 'globalTab' }" @click="changeTab('globalTab')">Activity</a>
        </b-dropdown-item>
        <b-dropdown-item v-if="nav_menu == 'Global' && Object.keys(additionalResource_1).length > 0">
          <a class="nav-link" :class="{ 'active': activeTab === 'RAG_1'  }" @click="changeTab('RAG_1')" >Activity1</a>
        </b-dropdown-item>
        <b-dropdown-item v-if="nav_menu == 'Global' && Object.keys(additionalResource_2).length > 0">
          <a class="nav-link" :class="{ 'active': activeTab === 'RAG_2'  }" @click="changeTab('RAG_2')" >Activity2</a>        
        </b-dropdown-item>
    </b-dropdown>
        <li class="nav-item">
          <a class="nav-link" :class="{ 'active': activeTab === 'evaluationTab' }" @click="changeTab('evaluationTab')">Evaluation</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" :class="{ 'active': activeTab === 'ProfileTab' }" @click="changeTab('ProfileTab')">Profile</a>
        </li>
      </ul>
      <div id="ActivitySequential" v-show="activeTab === 'sequentialTab'">
        <ResourcesViewsSequential v-if="activeTab === 'sequentialTab'" />
      </div>
      <div id="ActivityGlobal" v-show="activeTab === 'globalTab'">
        <ResourcesViewsGlobal v-if="activeTab === 'globalTab'" />
      </div>
      <div id="RASequential1" v-show="activeTab === 'RAS_1'">
        <ResourceAdditionalS_1 v-if="activeTab === 'RAS_1'" />
      </div>
      <div id="RASequential2" v-show="activeTab === 'RAS_2'">
        <ResourceAdditionalS_2 v-if="activeTab === 'RAS_2'" />
      </div>
      <div id="RAGlobal1" v-show="activeTab === 'RAG_1'">
        <ResourceAdditionalG_1 v-if="activeTab === 'RAG_1'" />
      </div>
      <div id="RAGlobal2" v-show="activeTab === 'RAG_2'">
        <ResourceAdditionalG_2 v-if="activeTab === 'RAG_2'" />
      </div>
      <div id="diagnosisStateEvaluation" v-show="activeTab === 'evaluationTab'">
        <diagnosis-state-evaluation v-if="activeTab === 'evaluationTab'" />
      </div>
      <div id="profile" v-show="activeTab === 'ProfileTab'">
        <Profile v-if="activeTab === 'ProfileTab'" />
      </div>
    </div>
  </template>
  
  <script>
  
  import Profile from './ProfileUser.vue';
  import ResourcesViewsGlobal from './ResourcesComponent/ResourcesViewGlobal.vue';
  import ResourcesViewsSequential from './ResourcesComponent/ResourcesViewSequential.vue';
  import ResourceAdditionalS_1 from './ResourcesComponent/AdditionalResources/AdditionalRsequential/additionalResourceS_1.vue'
  import ResourceAdditionalS_2 from './ResourcesComponent/AdditionalResources/AdditionalRsequential/additionalResourceS_2.vue'
  import ResourceAdditionalG_1 from './ResourcesComponent/AdditionalResources/AdditionalRglobal/additionalResourceG_1.vue'
  import ResourceAdditionalG_2 from './ResourcesComponent/AdditionalResources/AdditionalRglobal/additionalResourceG_2.vue'
  import DiagnosisStateEvaluation from './diagnosisStateEvaluation.vue';
  import axios from 'axios';

  /*import { BPopover } from 'bootstrap-vue';
*/
  
  export default {
    components: {
      ResourcesViewsGlobal,
      ResourcesViewsSequential,
      DiagnosisStateEvaluation,
      ResourceAdditionalG_1,
      ResourceAdditionalG_2,
      ResourceAdditionalS_1,
      ResourceAdditionalS_2,
      Profile
      /**/
    },
    data() {
      return {
        nav_menu: '', 
        activeTab: '', 
        additionalResource_1: [],
        additionalResource_2: [],
        isProfileSidebarOpen: false,
        showProfile: false

      };
    },
    mounted() {
      const id_student = this.$store.state.userId
      axios.get(`/api/Activity/${id_student}`) 
        .then(response => {
          this.nav_menu = response.data.nav_menu; 
          this.additionalResource_1 = response.data.resource_list_additional_1
          this.additionalResource_2 = response.data.resource_list_additional_2
          console.log('otros', this.additionalResource)
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
      toggleProfileSidebar() {
      this.isProfileSidebarOpen = !this.isProfileSidebarOpen;
    }
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

.profile-sidebar {
  width: 300px; 
  background-color: #ffffff; 
  padding: 20px; 
  position: fixed; 
  top: 0;
  bottom: 0;
  left: 0;
  overflow-y: auto; 
  box-shadow: 2px 0 4px rgba(0, 0, 0, 0.1);
}

.mobile-toggle-button {
  display: none; 
}

@media (max-width: 850px) {
  .mobile-toggle-button {
    display: block; 
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 1000;
  }
}
  </style>
  