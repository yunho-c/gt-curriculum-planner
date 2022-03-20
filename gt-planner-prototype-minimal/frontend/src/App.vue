<template>
  <h1>GT-Planner Prototype Minimal</h1>
  <!-- <button @click="fetch_graph">fetch_graph</button> -->
  <button @click="$refs.asdf.draw(d1)">draw1</button>
  <button @click="$refs.asdf.draw(d2)">draw2</button>
  <button @click="$refs.asdf.draw(d3)">draw3</button>
  <button @click="$refs.asdf.draw(d4)">draw4</button>
  <div id="graph" style="text-align: center;"/>
  <graph-div ref='asdf'/>
</template>

<script>
import GraphDiv from './components/GraphDiv.vue'

export default {
  name: 'App',
  data() {
    return {
      d1: 'digraph {a}',
      d2: 'digraph {a -> b}',
      d3: 'digraph {a -> b -> c}',
      d4: 'digraph {a -> b -> c -> d}',
    }
  },
  methods: {
    fetch_graph() {
      this.axios.get('http://localhost:8000/graph/0').then((response) => {
        this.d1 = response.data.item_id
      })
      this.axios.get('http://localhost:8000/graph/1').then((response) => {
        this.d2 = response.data.item_id
      })
      this.axios.get('http://localhost:8000/graph/2').then((response) => {
        this.d3 = response.data.item_id
      })
      this.axios.get('http://localhost:8000/graph/3').then((response) => {
        this.d4 = response.data.item_id
      })
    },
  },
  // (components registration:)
  components: {
    GraphDiv
  },

  mounted() {
    this.fetch_graph()
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
