<template>
  <div class="main-content">
    <Map />
  </div>
</template>

<script>
import Map from './Map.vue';

export default {
  name: "MainContent",
  components: {
    Map
  },
};
</script>

<style scoped lang="scss">
.main-content {
  height: 100vh;
}
</style>
