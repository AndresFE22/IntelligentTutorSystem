<template>
  <div id="app">
 <router-view></router-view>
  </div>
</template>

<style scoped>
</style>

<script>
export default {
  methods: {
    isActive(route) {
      return this.$route.path === route;
    }
  }
};
</script>
