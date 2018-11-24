<template>
  <div class="main-content">
    <div class="main-content__search">
      <input type="text" placeholder="Wpisz adres wydarzenia"/>
      <button>Utwórz</button>
    </div>
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
    position: relative;
    &__search {
      max-width: 640px;
      width: 100%;
      position: absolute;
      top: 80px;
      left: 0;
      right: 0;
      z-index: 1;
      margin: auto;
      box-sizing: border-box;
      display: flex;
      input {
        background: #fff;
        color: $black;
        font-size: 16px;
        font-weight: 600;
        line-height: 19px;
        flex: 1 1 auto;
        padding: 20px;
        border: 1px solid $black;
        &:placeholder-shown {
          font-weight: 400;
        }
      }

      button {
        background: $black;
        color: #fff;
        font-size: 16px;
        font-weight: 400;
        line-height: 19px;
        letter-spacing: 1px;
        padding: 20px 25px;
        flex: 0 0 auto;
        border: 0;
        cursor: pointer;
        &:hover {
          background: #000;
        }
      }
    }
  }
</style>
