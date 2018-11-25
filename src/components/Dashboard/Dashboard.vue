<template>
  <div class="dashboard">
      <sidebar :events="this.events" :filters="filters" :setFilter="setFilter" :allSelected="allSelected" class="dashboard__sidebar"/>
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
    allSelected: true,
    filters: [
      { name: 'heart attack', label: 'Zawał serca', checked: true },
      { name: 'accident', label: 'Wypadek', checked: true },
      { name: 'epilepsy', label: 'Atak padaczki', checked: true },
      { name: 'choking', label: 'Zadławienie', checked: true },
      { name: 'haemorrhage', label: 'Krwotoki', checked: true },
      { name: 'fracture', label: 'Złamania', checked: true }
    ]
  }),
  methods: {
    getEvents: function() {
      axios
      .get(`${apiUrl}/list/events`)
      .then(response => {
        this.events = response.data.filter(event => {
          return this.filters.filter(filter => filter.checked).map(filter => filter.name).includes(event._source.event_type);
        });
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
    setFilter(name, id, event){
      if(name === 'all'){
        this.allSelected = event.target.checked;
        this.filters.forEach(filter => filter.checked = event.target.checked);
      }else{
        this.filters[id].checked = event.target.checked;
      }
      this.getEvents();
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
