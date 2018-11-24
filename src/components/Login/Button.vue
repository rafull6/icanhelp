<template>
  <button class="button"><slot/></button>
</template>

<script>
export default {
  name: "Button"
};
</script>

<style scoped lang="scss">
  .button {
    color: #fff;
    background: $blue;
    font-family: 'Exo 2', sans-serif;
    font-weight: 600;
    font-size: 16px;
    text-align: center;
    padding: 17px 20px;
    box-sizing: border-box;
    width: 100%;
    border: 0;
    cursor: pointer;
    &:hover {
      background: lighten($blue, 5%);
    }

    &:active {
      background: darken($blue, 5%);
    }
  }
</style>
