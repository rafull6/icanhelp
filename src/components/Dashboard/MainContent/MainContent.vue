<template>
  <div class="main-content">
    <form class="main-content__search" v-on:submit.prevent="showTiles($event)">
      <input id="search-box" type="text" placeholder="Wpisz adres wydarzenia"/>
      <button>Utwórz</button>
    </form>
    <Map zoom="12" :users="this.users" :setAddress="setAddress"/>
    <div v-if="tilesVisible" class="types">
      <div class="types__content">
        <div class="types__head">
          <span class="types__address">{{ address.formatted_address }}</span>
          <a v-on:click.prevent="hideTiles()" href="">Wróć do widoku mapy</a>
        </div>
        <ul class="types__tiles">
          <li v-on:click="submitType('heart attack', $event)">Zawał serca<img src="@/assets/types/type1.png"/></li>
          <li v-on:click="submitType('accident', $event)">Wypadek<img src="@/assets/types/type2.png"/></li>
          <li v-on:click="submitType('epilepsy', $event)">Atak padaczki<img src="@/assets/types/type3.png"/></li>
          <li v-on:click="submitType('choking', $event)">Zadławienia<img src="@/assets/types/type4.png"/></li>
          <li v-on:click="submitType('haemorrhage', $event)">Krwotoki<img src="@/assets/types/type5.png"/></li>
          <li v-on:click="submitType('fracture', $event)">Złamania<img src="@/assets/types/type6.png"/></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Map from './Map.vue';
import EventBus from '@/event-bus.js';

export default {
  name: "MainContent",
  props: ['users'],
  components: {
    Map
  },
  data: () => ({
    address: null,
    type: null,
    tilesVisible: false
  }),
  methods: {
    showTiles: function(event) {
      if(this.address !== null){
        this.tilesVisible = true;
      }
    },
    hideTiles: function(){
      this.tilesVisible = false;
    },
    submitType: function(type, event) {
      this.tilesVisible = false;
      axios
        .post(`http://10.250.195.40:5000/add/event`, JSON.stringify({
          location: {
            lat: this.address.geometry.location.lat(),
            lon: this.address.geometry.location.lng()
          },
          status: 'default',
          event_type: type,
          address: this.address.formatted_address,
          description: '',
          timestamp: '2018-11-24T21:21:23.992203'
        }))
        .then(response => {
          console.log(response);
        })
        .catch(e => console.log(e));
    },
    setAddress: function(address){
      this.address = address;
    }
  },
  updated() {
    EventBus.$emit('update_map', this.users);
  }
};
</script>

<style scoped lang="scss">
  .main-content {
    position: relative;
    &__search {
      max-width: 800px;
      width: 100%;
      position: absolute;
      top: 70px;
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

  .types {
    background: #f5f5f5;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 2;
    display: flex;
    align-items: center;
    justify-content: center;
    &__content {
      max-width: 880px;
      width: 100%;
    }

    &__head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 15px;
      a {
        color: $blue;
        font-size: 14px;
        font-weight: 500;
        display: block;
        text-decoration: none;
        &:hover {
          text-decoration: underline;
        }
      }
    }

    &__address {
      color: #161616;
      font-size: 14px;
      font-weight: 500;
      display: block;
    }

    &__tiles {
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      grid-template-columns: auto auto;
      grid-auto-rows: 150px;
      grid-column-gap: 50px;
      grid-row-gap: 30px;
      > li {
        background: #fff;
        color: $black;
        font-size: 27px;
        font-weight: 600;
        padding: 20px 25px;
        box-sizing: border-box;
        position: relative;
        cursor: pointer;
        &:hover {
          background: linear-gradient(to right bottom, $lighter-blue, $blue);
          color: #fff;
          img {
            object-position: right top;
          }
        }

        img {
          position: absolute;
          bottom: 20px;
          right: 20px;
          object-fit: none;
          object-position: left top;
        }

        &:nth-child(1) img {
          width: 54px;
          height: 55px;
        }

        &:nth-child(2) img {
          width: 47px;
          height: 51px;
        }

        &:nth-child(3) img {
          width: 45px;
          height: 45px;
        }

        &:nth-child(4) img {
          width: 49px;
          height: 37px;
        }

        &:nth-child(5) img {
          width: 57px;
          height: 44px;
        }

        &:nth-child(6) img {
          width: 52px;
          height: 28px;
        }
      }
    }
  }
</style>
