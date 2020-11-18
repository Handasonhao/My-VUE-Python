<!--
 * @Author       : Wang.HH
 * @Date         : 2020-10-23 11:09:09
 * @LastEditTime : 2020-10-23 12:40:15
 * @LastEditors  : Wang.HH
 * @Description  : your description
 * @FilePath     : /My-VUE-Python/Vue/element-ui/src/pages/2/3.vue
-->
<template>
    <div>
        <div class="djsa">
            3333
            <el-button type="primary" size="default" @click="go"></el-button>
        </div>
    </div>
</template>

<script>
export default {
  methods: {
    go () {
      this.$router.go(-2)
    }
  }
}
</script>

<style>
.djsaP{
    color: lightcoral;
}
</style>
