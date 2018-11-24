<template>
  <div class="dashboard">
    <div class="dashboard__sidebar">
      <Sidebar /> 
    </div>
    <div class="dashboard__main-content">
      <MainContent />
    </div>
  </div>
</template>

<script>
import MainContent from './MainContent/MainContent.vue';
import Sidebar from './Sidebar/Sidebar.vue';

export default {
  name: "Dashboard",
  components: {
    MainContent,
    Sidebar
  }
};
</script>

<style scoped lang="scss">
.dashboard {
  display: flex;

  &__sidebar {
    width: 25%;
  }
  &__main-content {
    width: 75%;
  }
}
</style>
