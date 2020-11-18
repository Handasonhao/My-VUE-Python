<!--
 * @Author       : Wang.HH
 * @Date         : 2020-10-22 14:29:39
 * @LastEditTime : 2020-10-31 09:25:35
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
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data () {
    return {
      result: '',
      list: ['a', 'b', 'c', 'd'],
      // eslint-disable-next-line standard/object-curly-even-spacing
      inputdata: { a: 1, b: [1, 2, { c: true }, [3]], d: { e: 2, f: 3 }, g: null }
    }
  },
  created () {
    this.handleFun(1, 2, 3, 4)
    // this.flatten(this.inputdata)
    console.log(this.flatten(this.inputdata))
  },
  methods: {
    search () {
      console.log('aaaaaaaaaaaaaa')
      console.log('router:', this.$router)
      this.$router.push('/2222/3333')
      this.$router.push('3333')
    },
    handleFun (a, b, c, d) {
      this.result = Array.prototype.slice.call(arguments)
    },
    flatten (input, objkey = '') {
      let obj = {}
      let str = ''
      if (input instanceof Array) {
        for (let key in input) {
          str = objkey + '[' + key + ']'
          if (!(input[key] instanceof Array) && !(input[key] instanceof Object)) {
            obj[str] = input[key]
            // console.log(str, obj[str])
          }
          Object.assign(obj, this.flatten(input[key], str))
        }
      } else if (input instanceof Object) {
        for (let key in input) {
          str = objkey ? objkey + '.' + key : key
          if (!(input[key] instanceof Array) && !(input[key] instanceof Object)) {
            obj[str] = input[key]
            // console.log(str, obj[str])
          }
          Object.assign(obj, this.flatten(input[key], str))
        }
      }
      return obj
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
