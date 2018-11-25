<template>
  <div class="dashboard">
      <sidebar :events="this.events" class="dashboard__sidebar"/>
      <MainContent v-if="this.paramedics && this.events" :users="{paramedics: this.paramedics, events: this.events}" class="dashboard__main-content"/>
  </div>
</template>

<script>
import Sidebar from './Sidebar';
import MainContent from './MainContent/MainContent.vue';
import { apiUrl } from '@/utils/urls.js';
import axios from "axios";

export default {
  name: "Dashboard",
  components: { Sidebar, MainContent },
  data: () => ({
    events: null,
    paramedics: null,
  }),
  methods: {
    getEvents: function() {
      axios
      .get(`${apiUrl}/list/events`)
      .then(response => {
        this.events = response.data;
      })
      .catch(e => console.log(e));
    },
    getParamedics: function() {
      axios
      .get(`${apiUrl}/list/paramedics`)
      .then(response => {
        this.paramedics = response.data;
      })
      .catch(e => console.log(e));
    },
    initDashboard: function() {
      this.getEvents();
      this.getParamedics();
    },
    mapAdresses: function(events) {
      const geocoder = new google.maps.Geocoder;
      
      events.forEach((event, index) => {
        const latlng = {
          lat: parseFloat(event._source.location.lat),
          lng: parseFloat(event._source.location.lon)
        };
        geocoder.geocode({
          'location': latlng
        }, function (results, status) {
          if (status === 'OK') {
            if (results[0]) {
              events[index]._source.address = results[0].formatted_address;
            } else {
              window.alert('No results found');
            }
          } else {
            window.alert('Geocoder failed due to: ' + status);
          }
        });
      });
    }
  },
  created() {
    this.initDashboard();
  }
};
</script>

<style scoped lang="scss">
  .dashboard {
    flex: 1 1 auto;
    display: flex;
    overflow: hidden;
    width: 100%;
    height: 100%;
    &__sidebar {
      background: #fff;
      flex: 0 0 350px;
      position: relative;
      z-index: 4;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
    }

    &__main-content {
      background: $dark-blue;
      flex: 1 1 auto;
    }
  }
</style>
