<template>
  <div id="app">
    <router-view v-if="!this.loading" />
  </div>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    loading: true
  }),
  methods: {
    loadingChange: function() {
      this.loading = false;
    }
  },
  mounted() {
    const api = document.createElement('script');
    api.addEventListener('load', this.loadingChange);
    api.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBRFc0HsUJAA1JNf71DWH96Gs1Wdz6vb3E&libraries=places';
    document.body.appendChild(api);    
  }
};
</script>

<style lang="scss">
  #app {
    width: 100%;
    min-height: 100%;
  }
</style>
