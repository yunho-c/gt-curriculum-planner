<template>
  <div>
    <button @click="$refs.canvas.draw(d1)">1</button>
    <button @click="$refs.canvas.draw(d2)">2</button>
    <button @click="$refs.canvas.draw(d3)">3</button>
    <button @click="$refs.canvas.draw(d4)">4</button>
    <button>Optimize</button>
    <graph-div ref="canvas" />
  </div>
</template>

<script>
import GraphDiv from "../components/GraphDiv.vue";

export default {
  name: "MainPage",
  data() {
    return {
      d1: "digraph {a}",
      d2: "digraph {a -> b}",
      d3: "digraph {a -> b -> c}",
      d4: "digraph {a -> b -> c -> d}",
    };
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