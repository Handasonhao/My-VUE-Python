/*
 * @Author       : Wang.HH
 * @Date         : 2020-10-22 14:20:18
 * @LastEditTime : 2020-10-23 09:19:49
 * @LastEditors  : Wang.HH
 * @Description  : your description
 * @FilePath     : /My-VUE-Python/Vue/element-ui/src/main.js
 */
/* 主要作用是初始化vue实例并使用需要的插件 */
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false
Vue.use(ElementUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
