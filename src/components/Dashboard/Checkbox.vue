<template>
  <div class="checkbox" v-bind:class="{ white: type === 'white' }">
    <div class="checkbox__input"><input type="checkbox" :id="'checkbox-' + name" :name="name" :checked="checked" v-on:change="change(id, $event)"/><i/></div>
    <label class="checkbox__label" :for="'checkbox-' + name">{{ label }}</label>
  </div>
</template>

<script>
import EventBus from '@/event-bus.js';

export default {
  name: "Checkbox",
  props: {
    id: Number,
    name: String,
    label: String,
    type: String,
    checked: Boolean
  },
  methods: {
    change: (id, event) => {
      EventBus.$emit('checkbox_change', event, id);
    }
  },
  created() {
    this.on = this.checked;
  }
};
</script>

<style scoped lang="scss">
  .checkbox {
    display: flex;
    align-items: center;
    &__label {
      color: $black;
      font-size: 13px;
      font-weight: 400;
    }

    &__input {
      width: 10px;
      height: 10px;
      border: 2px solid $blue;
      position: relative;
      margin-right: 15px;
      input {
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0;
        border: 0;
        padding: 0;
        margin: 0;
        &:checked + i {
          background: $blue;
          position: absolute;
          left: 0;
          right: 0;
          top: 0;
          bottom: 0;
          pointer-events: none;
          display: block;
        }
      }
    }

    &.white {
      .checkbox {
        &__label {
          color: #fff;
        }

        &__input {
          border-color: #fff;
          input:checked + i {
            background: #fff;
          }
        }
      }
    }
  }
</style>
