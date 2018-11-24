<template>
  <div class="dashboard">
    <div class="dashboard__head">
      <img class="login__logo" alt="I Can Help" src="@/assets/logo.png"/>
      <div class="dashboard__avatar"><img src="@/assets/avatar.png"/></div>
    </div>
    <div class="dashboard__body">
      <sidebar class="dashboard__sidebar"/>
      <MainContent class="dashboard__main-content"/>
    </div>
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
    }

    &__avatar {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      overflow: hidden;
    }

    &__body {
      flex: 1 1 auto;
      display: flex;
    }

    &__sidebar {
      background: #fff;
      flex: 0 0 350px;
      position: relative;
    }

    &__main-content {
      background: $dark-blue;
      flex: 1 1 auto;
    }
  }
</style>
