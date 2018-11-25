<template>
  <div id="map"></div>
</template>

<script>
import { style, icons } from "@/utils/map.js";
import { geo } from "@/utils/geolocation.js";

export default {
  name: "Map",
  props: ["zoom", "users", "setAddress"],
  data: () => ({
    myLocation: null,
    events: {},
    map: null,
    marker: null,
    events: null,
    paramedics: null,
  }),
  methods: {
    createMarker: function(user, map) {
      const options = {
        position: new google.maps.LatLng(
          user._source.location.lat,
          user._source.location.lon
        ),
        title: user._source.status,
        map: map
      }
      if (user._source.status) {
        options.title = user._source.status;
        options.icon = icons[user._source.status].icon;
      } else if (user._source.type) {
        if (user._source.type === 'ambulance') {
          options.icon = icons['car'].icon;
        }else if(user._source.type === 'human') {
          options.icon = icons['human'].icon;
        }
      }
      const marker = new google.maps.Marker(options);
    },
    getLocation: function() {
      this.myLocation = geo.passive;
    },
    showUsers: function(groups, map) {
      for(const group in groups) {
        groups[group].forEach(user => {
          this.createMarker(user, map);
        });
      }
    },
    renderMap: function() {
      const that = this;
      const mapOptions = {
        zoom: parseInt(this.zoom, 10),
        center: new google.maps.LatLng(
          parseFloat(geo.passive.lat),
          parseFloat(geo.passive.lng)
        ),
        styles: style,
        mapTypeControl: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      const mapElement = document.getElementById("map");
      this.map = new google.maps.Map(mapElement, mapOptions);
      this.showUsers(this.users, this.map);
      
      this.marker = new google.maps.Marker({
        icon: icons['default'].icon,
        title: 'default',
        map: this.map
      });

      const input = document.getElementById('search-box');
      if(input){
        const options = { componentRestrictions: {country: 'pl'} };
        const autocomplete = new google.maps.places.Autocomplete(input, options);
        autocomplete.bindTo('bounds', this.map);

        autocomplete.addListener('place_changed', function() {
          const place = autocomplete.getPlace();
          that.marker.setPosition(place.geometry.location);
          that.marker.setVisible(true);
          that.map.setCenter(place.geometry.location);
          that.map.setZoom(14);
          that.setAddress(place);
        });
      }
    }
  },
  mounted() {
    this.renderMap();
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

  .tooltip {
    background: linear-gradient(to bottom, #275381, #1f466f);
    width: 174px;
    text-align: center;
    position: relative;
    z-index: 1;
    &:after {
      background: $lighter-blue;
      width: 20px;
      height: 20px;
      display: block;
      content: '';
      transform: rotate(45deg);
      position: absolute;
      bottom: -10px;
      left: 0;
      right: 0;
      margin: auto;
      z-index: -1;
    }

    &__avatar {
      display: block;
      margin: 0 auto 20px;
    }

    &__name {
      color: #fff;
      text-transform: uppercase;
      font-size: 16px;
      font-weight: 600;
      margin: 0;
    }

    &__age {
      color: #64e7ff;
      font-weight: 400;
      display: block;
      margin-bottom: 15px;
    }

    &__specjalization {
      color: #cff8ff;
      font-size: 14px;
      font-weight: 400;
      display: block;
      margin-bottom: 20px;
    }

    &__button {
      background: $lighter-blue;
      color: #fff;
      font-weight: 400;
      width: 100%;
      border: 0;
      text-align: center;
      text-transform: uppercase;
      padding: 10px 0;
      cursor: pointer;
      &:hover {
        background: lighten($blue, 5%);
      }

      &:active {
        background: darken($blue, 5%);
      }
    }
  }
</style>
