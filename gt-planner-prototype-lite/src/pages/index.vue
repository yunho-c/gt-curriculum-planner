<template>
  <bg />
  <div id="a">
    <div text-9xl fw400 op90>
      GT Planner
    </div>
    <div op70 text-lg fw400 m1 hover="op80" transition="200">
      Better curriculum planning.
    </div>
    <div ma style="width: 50%">
      <v-select id="b" v-model="selected_major" class="m-3 text-lg" background-color="white" :options="majors" placeholder="Major" />
      <v-select v-if="selected_major" id="c" v-model="selected_thread" class="m-3 text-lg" background-color="white" :options="selected_major.threads" placeholder="Threads" />
      <button class="m-3 text-sm btn" @click="start">
        Start
      </button>
    </div>
  </div>
  <div absolute bottom-5 right-0 left-0 text-center text-xl op70 fw300>
    <!-- about · feedback -->
    <a href="/about">about</a> · <a href="mailto:yunhoyunho@gatech.edu">feedback</a>
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
      selected_thread: null,
      majors: [
        {
          id: 0,
          label: 'CS',
          threaded: true,
          multithreaded: true,
          threads: [
            'Devices',
            'Information Internetworks',
            'Intelligence',
            'Media',
            'Modeling',
            'People',
            'Systems and Architecture',
            'Theory',
          ],
        },
        {
          id: 1,
          label: 'ME',
          threaded: true,
          threads: [
            'None',
            'Automation and Robotics',
            'Automative Engineering',
            'Design',
            'Manufacturing',
            'Mechanics of Materials',
            'Micro- and Nano- Engineering',
            'Nuclear Energy',
            'Thermal, Fluid, and Energy Systems',
          ],
        },
        {
          id: 2,
          label: 'Business',
          threaded: true,
          threads: [
            'TODO',
          ],
        },
        {
          id: 3,
          label: 'ISyE',
          threaded: true,
          threads: [
            'TODO',
          ],
        },
        {
          id: 4,
          label: 'BME',
          threaded: true,
          multithreaded: false,
          threads: [
            'TODO',
          ],
        },
        {
          id: 5,
          label: 'EE',
          threaded: true,
          multithreaded: false,
          threads: [
            'TODO',
          ],
        },
        {
          id: 6,
          label: 'CE',
          threaded: true,
          multithreaded: false,
          threads: [
            'TODO',
          ],
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

      this.axios.get(`https://backend.gt-planner.com/curr/${this.selected_major.label}`).then((response) => {
        this.curr = response.data
        localStorage.setItem('courses', JSON.stringify(this.curr))
      })
    },
    load_curr() {
      const courses = JSON.parse(localStorage.getItem('courses'))
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
#b,
#c
{
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
