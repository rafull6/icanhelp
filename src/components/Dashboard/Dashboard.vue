<template>
  <div class="dashboard">
    <sidebar class="dashboard__sidebar"/>
    <MainContent class="dashboard__main-content"/>
  </div>
</template>

<script>
import Sidebar from './Sidebar';
import MainContent from './MainContent/MainContent.vue';

export default {
  name: "Dashboard",
  components: { Sidebar, MainContent }
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
