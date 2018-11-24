<template>
  <div class="main-content">
    <Map />
  </div>
</template>

<script>
import Map from './Map.vue';

export default {
  name: "MainContent",
  components: {
    Map
  },
  mounted() {
    console.log(google.maps.Map);
    console.log('chuj')
    const map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });
  }
};
</script>

<style scoped lang="scss">
.main-content {
  height: 100vh;
}
</style>
