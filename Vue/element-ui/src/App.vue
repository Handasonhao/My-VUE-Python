<!--
 * @Author       : Wang.HH
 * @Date         : 2020-10-22 14:20:18
 * @LastEditTime : 2020-10-23 09:16:40
 * @LastEditors  : Wang.HH
 * @Description  : your description
 * @FilePath     : /My-VUE-Python/Vue/element-ui/src/App.vue
-->
<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view/> <!-- 是子路由视图，后面的路由页面都显示在此处，相当于一个指示标，指引显示哪个页面。 -->
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url('./assets/css/my_style.css');
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
