<template>
  <div>
    <div>
      <v-select :options="majors" placeholder="Major"/>
      <button @click="fetch_curr">Fetch Curriculum</button>
    </div>
    <!-- checkbox for debug -->
    <br>
    Completed:
    <div v-for="(content, course) in curr" :key="course.id">
      <label>{{course}}</label>
      <input type="checkbox" v-model="content.done" :value="course"/>
    </div>
  </div>
</template>

<script>
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'

export default {
  name: 'SetupPage',
  data() {
    return {
      a: 'b',
      b: 'd',
      majors: [
        {
          id: 0,
          label: 'ME'
        },
        {
          id: 1,
          label: 'BME'
        },
      ],
      curr: false
    }
  },
  methods: {
    fetch_curr() {
      this.axios.get('http://localhost:8000/curr/ME').then((response) => {
        this.curr = response.data
        // console.log(response.data)
        // console.log(response)
      })
    },
  },
  components: {
    vSelect
  },
  mounted() {
    // this.fetch_curr()
  }
}
</script>