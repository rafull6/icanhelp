<template>
  <div class="dashboard">
    <div class="dashboard__head">
      <img class="login__logo" alt="I Can Help" src="@/assets/logo.png"/>
    </div>
    <div class="dashboard__body">
      <sidebar class="dashboard__sidebar"/>
        <MainContent v-if="!this.loading" :events="this.events" class="dashboard__main-content"/>
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
    events: {},
    loading: true
  }),
  methods: {
    getEvents: function() {
      axios
      .get(`${apiUrl}/list/events`)
      .then(response => {
        this.events = response.data;
        this.loading = false;
        console.log(this.loading)
      })
      .catch(e => console.log(e));
    }
  },
  created() {
    this.getEvents();
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
