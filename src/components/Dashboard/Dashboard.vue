<template>
  <div class="hello">
    Dashboard page
    <div id="map"></div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  props: {
    msg: String
  },
  mounted() {
    console.log(google.maps.Map);

      const map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });
  }
// mounted() {
  //   console.log('object')
  //   const api = document.createElement('script');
  //   api.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBRFc0HsUJAA1JNf71DWH96Gs1Wdz6vb3E";
  //   api.onload = () => {
  //     map = new google.maps.Map(document.getElementById('map'), {
  //       center: {lat: -34.397, lng: 150.644},
  //       zoom: 8
  //     });
  //     console.log(map)
  //   }
  // },
};
</script>

<style scoped lang="scss">
#map {
  background: red;
  width: 500px;
  height: 300px;
}
</style>
