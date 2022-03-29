<template>
  <bg />
  <div id="a">
    <div text-9xl fw400>
      GT Planner
    </div>
    <div op50 text-lg fw400 m1 hover="op80" transition="200">
      Better curriculum planning.
    </div>
    <div ma style="width: 50%">
      <v-select id="b" class="m-3 text-lg" background-color="white" :options="majors" v-model="selected_major" placeholder="Major" />
      <button class="m-3 text-sm btn" @click="start">Start</button>
    </div>
  </div>
  <div absolute bottom-5 right-0 left-0 text-center text-xl op30 fw300>
    about · feedback
  </div>
</template>

<script lang="ts">
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'

import bg from '~/components/tr.vue'

export default {
  name: 'SetupPage',
  components: {
    bg,
    vSelect,
  },
  data() {
    return {
      curr: null,
      selected_major: null,
      majors: [
        {
          id: 0,
          label: 'ME',
        },
        {
          id: 1,
          label: 'BME',
        },
        {
          id: 2,
          label: 'CS',
        },
      ],
    }
  },
  mounted() {
    this.load_curr()
  },
  methods: {
    start() {
      this.fetch_curr()
      this.$router.push('/main')
    },
    fetch_curr() {
      console.log(this.selected_major)

      this.axios.get('http://localhost:8000/curr/'+this.selected_major.label).then((response) => {
        this.curr = response.data
        localStorage.setItem("courses", JSON.stringify(this.curr))
      });
    },
    load_curr() {
      const courses = JSON.parse(localStorage.getItem("courses"))
      if (courses != null) this.curr = courses
    },
  },
}
</script>

<style>
div {
  /* position: relative; */
  z-index: 1;
}
#a {
  position: relative;
  z-index: 2;
}
#b {
  --vs-controls-color: #c39d4c;
  --vs-border-color: #c39d4c;

  --vs-dropdown-bg: #282c34;
  --vs-dropdown-color: #cdbf99;
  --vs-dropdown-option-color: #cdbf99;

  --vs-selected-bg: #c39d4c;
  --vs-selected-color: #eeeeee;

  --vs-search-input-color: #eeeeee;
  --vs-search-input-placeholder-color: rgba(150,150,150);

  --vs-dropdown-option--active-bg: #c39d4c;
  --vs-dropdown-option--active-color: #eeeeee;
}
</style>
