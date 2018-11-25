<template>
  <div class="app">
    <div class="app__header">
      <img class="app__logo" alt="I Can Help" src="@/assets/logo.png"/>
    </div>
    <div class="app__map">
      <Map zoom="11" v-if="this.paramedics && this.events" :users="{paramedics: this.paramedics, events: this.events}" />
    </div>
    <div class="app__info">
      <div>
        <span>Aktualna interwencja:</span>
        <strong>Czarnowiejska 12</strong>
      </div>
      <div>
        <span>Odległość:</span>
        <strong>759 m</strong>
      </div>
    </div>
    <div class="app__desc">
      <span>Opis zgłoszenia:</span>
      <p>
        Kobieta w stanie ciężkim, walczy o życie, zawał serca, potrzebna pomoc
      </p>
    </div>
    <button class="app__button">Potwierdź pomoc</button>
  </div>
</template>

<script>
import Map from '../Dashboard/MainContent/Map.vue';
import axios from "axios";
import { apiUrl } from '@/utils/urls.js';

export default {
  name: "Mobile",
  components: { Map },
    data: () => ({
    events: null,
    paramedics: null,
    allSelected: true,
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
  .app {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    &__header {
      flex: 0 0 60px;
      display: flex;
      align-items: center;
      padding: 0 15px;
    }

    &__logo {
      height: 35px;
    }

    &__map {
      background: #f0f0f0;
      flex: 1 1 auto;
      width: 100%;
      height: 100%;
    }

    &__info {
      background: $blue;
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 20px 15px;
      span {
        color: #c1f6ff;
        text-transform: uppercase;
        font-size: 12px;
        font-weight: 600;
        display: block;
      }

      strong {
        color: #fff;
        font-size: 20px;
        font-weight: 400;
        margin: 0;
      }
    }

    &__desc {
      flex: 0 0 100px;
      overflow: auto;
      padding: 15px;
      > span {
        color: $blue;
        text-transform: uppercase;
        font-size: 12px;
        font-weight: 600;
        display: block;
        margin-bottom: 10px;
      }

      > p {
        color: $black;
        font-size: 16px;
        margin: 0;
      }
    }

    &__button {
      background: $black;
      color: #fff;
      border: 0;
      flex: 0 0 auto;
      font-size: 18px;
      font-weight: 600;
      text-transform: uppercase;
      text-align: center;
      padding: 20px 0;
    }
  }
</style>
