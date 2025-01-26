<template>
  <div ma>
    <p>
      <router-link to="/">
        Home
      </router-link>
    </p>
    <!-- <p>
      <em text-sm op75>Opinionated Vite Starter Template</em>
    </p> -->

    <div py-4 />
    <graph-div ref="gd" />
    <div>
      <input id="checkbox" v-model="checked" type="checkbox">
      <label for="checkbox">Use Pyodide (client-side graph computation)</label>
      <button
        class="m-3 text-sm btn"
        @click="optimize"
      >
        Optimize
      </button>
      <button
        class="m-3 text-sm btn"
        @click="fetch_example_graphs"
      >
        Fetch Example Graphs
      </button>
      <button
        class="m-3 text-sm btn"
        @click="draw_dot(ex_graph1)"
      >
        1
      </button>
      <button
        class="m-3 text-sm btn"
        @click="draw_dot(ex_graph2)"
      >
        2
      </button>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      dot: null,
      ex_graph1: null,
      ex_graph2: null,
      ex_graph3: null,
      ex_graph4: null,
      checked: false,
    }
  },
  mounted() {
    // this.name = $ref('')
    this.router = useRouter()
    this.curr = JSON.parse(localStorage.getItem('courses'))
    this.draw_graph(this.curr)
  },
  methods: {
    draw_dot(dot) {
      this.$refs.gd.draw(dot)
    },
    draw_graph(curr) {
      this.axios.post('http://localhost:8000/graph', { curr }).then((response) => {
        this.$refs.gd.draw(response.data)
        return response.data
      })
    },
    fetch_example_graphs() {
      this.axios.get('http://localhost:8000/example_graph/0').then((response) => {
        this.ex_graph1 = response.data.item_id
      })
      this.axios.get('http://localhost:8000/example_graph/1').then((response) => {
        this.ex_graph2 = response.data.item_id
      })
      this.axios.get('http://localhost:8000/example_graph/2').then((response) => {
        this.ex_graph3 = response.data.item_id
      })
      this.axios.get('http://localhost:8000/example_graph/3').then((response) => {
        this.ex_graph4 = response.data.item_id
      })
    },
    optimize() {
      this.curr = JSON.parse(localStorage.getItem('courses'))
      this.draw_graph(this.curr)
    },
    go_dynamic() {
      if (this.name) this.router.push(`/hi/${encodeURIComponent(name)}`)
    },
  },
}
</script>
