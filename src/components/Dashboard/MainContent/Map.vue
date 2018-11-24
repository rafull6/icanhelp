<template>
  <div id="map"></div>
</template>

<script>
export default {
  name: "Map",
  mounted() {
    console.log(google.maps.Map);
    const map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });
  }
};
</script>

<style scoped lang="scss">
#map {
  width: 100%;
  height: 100%;
}
</style>
