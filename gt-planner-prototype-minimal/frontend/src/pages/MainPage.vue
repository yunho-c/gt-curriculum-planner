<template>
  <button @click="fetch_example_graphs">Fetch Example graphs</button>
  <button @click="$refs.asdf.draw(ex_graph1)">1</button>
  <button @click="$refs.asdf.draw(ex_graph2)">2</button>
  <button @click="$refs.asdf.draw(ex_graph3)">3</button>
  <button @click="$refs.asdf.draw(ex_graph4)">4</button>
  <button>Optimize</button>
  <graph-div ref='asdf'/>

</template>

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
    }
  },
  methods: {
    fetch_example_graphs() {
      this.axios.get("http://localhost:8000/graph/0").then((response) => {
        this.d1 = response.data.item_id;
      });
      this.axios.get("http://localhost:8000/graph/1").then((response) => {
        this.d2 = response.data.item_id;
      });
      this.axios.get("http://localhost:8000/graph/2").then((response) => {
        this.d3 = response.data.item_id;
      });
      this.axios.get("http://localhost:8000/graph/3").then((response) => {
        this.d4 = response.data.item_id;
      });
    },
  },
  // (components registration:)
  components: {
    GraphDiv,
  },

  mounted() {
    this.fetch_example_graphs();
  },
};
</script>