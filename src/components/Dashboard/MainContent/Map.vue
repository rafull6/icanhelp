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
        title: feature.title ? feature.title : null,
        map: map
      });
    });
  }
};
</script>

<style lang="scss">
@-moz-keyframes pulsate {
  from {
    -moz-transform: scale(0.25);
    opacity: 1;
  }
  95% {
    -moz-transform: scale(1.3);
    opacity: 0;
  }
  to {
    -moz-transform: scale(0.3);
    opacity: 0;
  }
}
@-webkit-keyframes pulsate {
  from {
    -webkit-transform: scale(0.25);
    opacity: 1;
  }
  95% {
    -webkit-transform: scale(1.3);
    opacity: 0;
  }
  to {
    -webkit-transform: scale(0.3);
    opacity: 0;
  }
}

#map {
  width: 100%;
  height: 100%;
}

#map div[title="active"] {
  -moz-animation: pulsate 1.5s ease-in-out infinite;
  -webkit-animation: pulsate 1.5s ease-in-out infinite;
  border: 1pt solid #fff;
  -moz-border-radius: 51px;
  -webkit-border-radius: 51px;
  border-radius: 51px;
  -moz-box-shadow: inset 0 0 5px $red, inset 0 0 5px $red, inset 0 0 5px $red,
    0 0 5px $red, 0 0 5px $red, 0 0 5px $red;
  -webkit-box-shadow: inset 0 0 5px $red, inset 0 0 5px $red, inset 0 0 5px $red,
    0 0 5px $red, 0 0 5px $red, 0 0 5px $red;
  box-shadow: inset 0 0 5px $red, inset 0 0 5px $red, inset 0 0 5px $red,
    0 0 5px $red, 0 0 5px $red, 0 0 5px $red;
  height: 51px !important;
  margin: -15px 0 0 -15px;
  width: 51px !important;
}
#map div[title="active"] img {
  display: none;
}
@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
  only screen and (device-width: 768px) {
  #map div.gmnoprint[title="active"] {
    margin: -10px 0 0 -10px;
  }
}
</style>
