<template>
  <button @click="fetch_example_graphs">Fetch Example graphs</button>
  <button @click="$refs.asdf.draw(ex_graph1)">1</button>
  <button @click="$refs.asdf.draw(ex_graph2)">2</button>
  <button @click="$refs.asdf.draw(ex_graph3)">3</button>
  <button @click="$refs.asdf.draw(ex_graph4)">4</button>
  <button @click="optimize">Optimize</button>
  <graph-div ref='asdf'/>

</template>

<style>
/* @import url('https://fonts.googleapis.com/css2?family=Azeret+Mono:wght@300&display=swap'); */
@import url('https://fonts.googleapis.com/css2?family=Roboto+Serif:wght@400&display=swap');
</style>

<script>
import GraphDiv from "../components/GraphDiv.vue";

export default {
  name: "MainPage",
  data() {
    return {
      ex_graph1: 'digraph {a}',
      ex_graph2: 'digraph {a -> b}',
      ex_graph3: 'digraph {a -> b -> c}',
      ex_graph4: 'digraph {a -> b -> c -> d}',
      curr: null,
      graph: null
    }
  },
  methods: {
    fetch_example_graphs() {
      this.axios.get("http://localhost:8000/example_graph/0").then((response) => {
        this.ex_graph1 = response.data.item_id;
      });
      this.axios.get("http://localhost:8000/example_graph/1").then((response) => {
        this.ex_graph2 = response.data.item_id;
      });
      this.axios.get("http://localhost:8000/example_graph/2").then((response) => {
        this.ex_graph3 = response.data.item_id;
      });
      this.axios.get("http://localhost:8000/example_graph/3").then((response) => {
        this.ex_graph4 = response.data.item_id;
      });
    },
    fetch_graph(curr) {
      this.axios.post("http://localhost:8000/graph", {"curr": curr}).then((response) => {
        // this.graph = response.data
        this.$refs.asdf.draw(response.data)
        return response.data
      })
    },
    optimize() {
      this.curr = JSON.parse(localStorage.getItem("courses"));
      this.fetch_graph(this.curr)
    }
  },
  // (components registration:)
  components: {
    GraphDiv,
  },

  mounted() {
    this.fetch_example_graphs();
    this.curr = JSON.parse(localStorage.getItem("courses"));
    this.fetch_graph(this.curr)
  },
};
</script>