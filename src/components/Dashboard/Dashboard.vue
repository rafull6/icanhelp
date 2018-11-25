<template>
  <div class="dashboard">
    <div class="dashboard__head">
      <img class="login__logo" alt="I Can Help" src="@/assets/logo.png"/>
    </div>
    <div class="dashboard__body" v-if="!this.loading">
      <sidebar :events="this.events" class="dashboard__sidebar"/>
      <MainContent :users="{ambulance: this.ambulance, human: this.human}" class="dashboard__main-content"/>
    </div>
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
    events: [],
    ambulance: [],
    human: [],
    loading: true,
  }),
  methods: {
    getUsers: function(type) {
      axios
      .get(`${apiUrl}/list/${type}`)
      .then(response => {
        this.loading = false;
        if (type === 'events') {
          this.mapAdresses(response.data);
          this.events = response.data;
        } else if (type === 'paramedics') {
          response.data.map(item => {
            if (item._source.type === 'ambulance') {
              this.ambulance.push(item);
            } else {
              this.human.push(item);
            }
          })

        }
      })
      .catch(e => console.log(e));
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
    this.getUsers('events');
    this.getUsers('paramedics');
  }
};
</script>

<style scoped lang="scss">
  .dashboard {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    &__head {
      flex: 0 0 80px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 25px;
      box-shadow: 0 0 15px rgba(0,0,0,0.3);
      position: relative;
      z-index: 3;
    }

    &__body {
      flex: 1 1 auto;
      display: flex;
      overflow: hidden;
    }

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
