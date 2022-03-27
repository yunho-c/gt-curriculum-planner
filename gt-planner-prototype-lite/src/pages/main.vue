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
      <button
        class="m-3 text-sm btn"
        @click="optimize" 
      >
        Optimize
      </button>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      dot: null,
    }
  },
  mounted() {
    // this.name = $ref('')
    this.router = useRouter()
    this.curr = JSON.parse(localStorage.getItem("courses"))
    this.draw_graph(this.curr)
  },
  methods: {
    draw_graph(curr) {
      this.axios.post("http://localhost:8000/graph", {"curr": curr}).then((response) => {
        this.$refs.gd.draw(response.data)
        return response.data
      })
    },
    optimize() {
      this.curr = JSON.parse(localStorage.getItem("courses"));
      this.draw_graph(this.curr)
    },
    go_dynamic() {
      if (this.name) this.router.push(`/hi/${encodeURIComponent(name)}`)
    },
  },
}
</script>
