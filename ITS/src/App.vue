<template>
  <div id="app">
        <router-view></router-view>
  </div>
</template>

<style scoped>
</style>

<script>

export default {
  data() {
    return {
      session: false
    }
  },

  methods: {
    isActive(route) {
      return this.$route.path === route;
    },
  }
};
</script>
