<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
    background-color: #fff;
}
::-webkit-scrollbar-thumb {
    border-radius:5px;
    background-color: rgba(0, 0, 0, 0.1)
}
.el-transfer-panel{
        width: 400px;
        height: 500px;
    }
.el-transfer-panel__list.is-filterable{
        height: 400px;
    }
</style>
