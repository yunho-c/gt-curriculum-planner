<template>
  <h1>GT-Planner Prototype Minimal</h1>
    <p>
    <router-link to="/setup">Setup</router-link>
    <router-link to="/">Main</router-link>
  </p>
  <router-view/>
  <!-- <button @click="fetch_graph">fetch_graph</button> -->


</template>

<script>

export default {
  name: 'App',
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
