<template>
  <div id="map"></div>
</template>

<script>
import { style, icons } from "@/utils/map.js";
import { generatedData } from "@/utils/data.js";

export default {
  name: "Map",
  props: ["zoom"],
  mounted() {
    var mapOptions = {
      zoom: 16,
      center: new google.maps.LatLng(-33.91722, 151.23064),
      styles: style
    };
    var mapElement = document.getElementById("map");
    var map = new google.maps.Map(mapElement, mapOptions);

    generatedData(google).forEach(function(feature) {
      const marker = new google.maps.Marker({
        position: feature.position,
        icon: icons[feature.type].icon,
        map: map
      });
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
