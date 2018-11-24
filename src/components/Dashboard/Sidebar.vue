<template>
  <div class="sidebar">
    <div class="sidebar__head">
      <h2>Filtry</h2>
      <checkbox name="all" label="Zaznacz wszystkie" :checked="allSelected" type="white"/>
    </div>
    <ul class="sidebar__filters">
      <li v-for="(filter, index) in filters" :key="index">
        <checkbox :name="filter.name" :label="filter.label" :checked="filter.checked" :id="index"/>
      </li>
    </ul>
    <div class="sidebar__head">
      <h2>Aktualne interwencje</h2>
      <span>Status</span>
    </div>
    <ul class="sidebar__accidents">
      <li>Czarnowiejska</li>
      <li class="volunteer">Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li class="ambulance">Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li class="volunteer">Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li class="ambulance">Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li class="volunteer">Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li class="ambulance">Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li class="volunteer">Czarnowiejska</li>
      <li>Czarnowiejska</li>
      <li class="ambulance">Czarnowiejska</li>
      <li>Czarnowiejska</li>
    </ul>
  </div>
</template>

<script>
import EventBus from '@/event-bus.js';
import Checkbox from './Checkbox';

export default {
  data: () => ({
    allSelected: true,
    filters: [
      { name: 'heart', label: 'Zawał serca', checked: true },
      { name: 'crush', label: 'Wypadek', checked: true },
      { name: 'epilepsy', label: 'Atak padaczki', checked: true },
      { name: 'choking', label: 'Zadławienie', checked: true },
      { name: 'blood', label: 'Krwotoki', checked: true },
      { name: 'brokens', label: 'Złamania', checked: true }
    ]
  }),
  name: "Sidebar",
  components: { Checkbox },
  created() {
    EventBus.$on('checkbox_change', (event, id) => {
      const name = event.target.name;
      if(name === 'all'){
        this.allSelected = event.target.checked;
        this.filters.forEach(filter => filter.checked = event.target.checked);
      }else{
        this.filters[id].checked = event.target.checked;
      }
    });
  }
};
</script>

<style scoped lang="scss">
  .sidebar {
    display: flex;
    flex-direction: column;
    &__head {
      background: linear-gradient(to right, $lighter-blue, $blue);
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 20px 25px;
      > h2 {
        color: #fff;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        margin: 0;
      }

      > span {
        color: #fff;
        font-size: 12px;
        text-transform: uppercase;
      }
    }

    &__filters {
      flex: 0 0 auto;
      list-style: none;
      padding: 25px 25px 10px;
      margin: 0;
      display: flex;
      flex-wrap: wrap;
      > li {
        margin-bottom: 20px;
        &:nth-child(odd){
          flex: 0 0 53.4%;
        }

        &:last-child {
          margin-bottom: 0;
        }
      }
    }

    &__accidents {
      flex: 1 1 auto;
      overflow: auto;
      list-style: none;
      margin: 0;
      padding: 0;
      height: 0;
      > li {
        color: $black;
        font-size: 15px;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 20px 20px 25px;
        &:after {
          content: '';
          background: $red;
          width: 20px;
          height: 20px;
          display: block;
          border-radius: 50%;
        }

        &:nth-child(even) {
          background: $gray;
        }

        &.volunteer:after {
          background: $dark-blue;
        }

        &.ambulance:after {
          background: $blue;
        }
      }

      /* width */
      &::-webkit-scrollbar {
          width: 12px;
      }

      /* Track */
      &::-webkit-scrollbar-track {
          background: #ececec; 
      }

      /* Handle */
      &::-webkit-scrollbar-thumb {
          background: #d5d5d5; 
          border-radius: 12px;
      }

      /* Handle on hover */
      &::-webkit-scrollbar-thumb:hover {
          background: #c0c0c0; 
      }
    }
  }
</style>
