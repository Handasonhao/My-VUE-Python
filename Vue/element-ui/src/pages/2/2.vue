/* eslint-disable space-before-function-paren */
<!--
 * @Author       : Wang.HH
 * @Date         : 2020-10-22 14:29:39
 * @LastEditTime : 2020-10-22 16:45:41
 * @LastEditors  : Wang.HH
 * @Description  : your description
 * @FilePath     : /My-VUE-Python/Vue/element-ui/src/pages/2/2.vue
-->
<template>
  <div>
    <i class="el-icon-edit"></i>
    <i class="el-icon-share"></i>
    <i class="el-icon-delete"></i>
    <el-button type="primary" icon="el-icon-search">搜索</el-button>
    <el-button type="primary" size="default" @click="search"></el-button>
    <div>{{ result }}-aaaaaa</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      result: '',
      list: ['a', 'b', 'c', 'd']
    }
  },
  created () {
    this.handleFun(1, 2, 3, 4)
  },
  methods: {
    search () {
      console.log('aaaaaaaaaaaaaa')
    },
    handleFun (a, b, c, d) {
      this.result = Array.prototype.slice.call(arguments)
    }
  }
}
</script>

<style scoped>
.aaa {
  color: seagreen;
  background-color: skyblue;
}
</style>
