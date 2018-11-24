<template>
  <div id="map"></div>
</template>

<script>
import { style, icons } from "@/utils/map.js";
import { geo } from "@/utils/geolocation.js";
import { generatedData } from "@/utils/data.js";

export default {
  name: "Map",
  props: ["zoom", "events"],
  data: () => ({
    myLocation: null
  }),
  methods: {
    getLocation: function(bool) {
      this.myLocation = bool
        ? this.$getLocation(geo.active).then(
            coordinates => (this.myLocation = coordinates)
          )
        : (this.myLocation = geo.passive);

        console.log(this.myLocation)
    },
    showEvents: function(events, map) {
      events.forEach(event => {
        const marker = new google.maps.Marker({
          position: new google.maps.LatLng(
            event._source.location.lat,
            event._source.location.lon
          ),
          icon: icons[event._source.status].icon,
          title: event._source.status,
          map: map
        });
      });
    },
    renderMap: function() {
      console.log('r', this.myLocation)
      const mapOptions = {
        zoom: parseInt(this.zoom, 10),
        center: new google.maps.LatLng(
          this.myLocation.lat,
          this.myLocation.lng
        ),
        styles: style
      };
      const mapElement = document.getElementById("map");
      const map = new google.maps.Map(mapElement, mapOptions);
      this.showEvents(this.events, map);
    }
  },
  watch: {
    myLocation: function() {
      console.log("myLocation", this.myLocation)
      this.renderMap();
    }
  },
  created() {
    this.getLocation(false);
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

#map div[title="default"] {
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
