<template>
  <div class="form-field">
    <label class="form-field__label">{{ label }}</label>
    <input class="form-field__input" :name="name" :type="type" :placeholder="placeholder"/>
  </div>
</template>

<script>
export default {
  name: "FormField",
  props: {
    label: String,
    name: String,
    type: String,
    placeholder: String
  }
};
</script>

<style scoped lang="scss">
  .form-field {
    margin-bottom: 25px;
    display: block;
    &__label {
      color: $blue;
      font-family: 'Exo 2', sans-serif;
      font-weight: 600;
      font-size: 15px;
      display: block;
      margin-bottom: 10px;
    }

    &__input {
      color: $black;
      background: rgba(255,255,255,0.8);
      font-family: 'Exo 2', sans-serif;
      font-size: 16px;
      font-weight: 600;
      display: block;
      width: 100%;
      border: 1px solid $blue;
      box-sizing: border-box;
      padding: 15px 20px;
      &:placeholder-shown {
        font-weight: 400;
      }
    }
  }
</style>
