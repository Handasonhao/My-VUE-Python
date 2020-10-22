/*
 * @Author       : Wang.HH
 * @Date         : 2020-10-22 14:20:18
 * @LastEditTime : 2020-10-22 15:31:08
 * @LastEditors  : Wang.HH
 * @Description  : your description
 * @FilePath     : /My-VUE-Python/Vue/element-ui/src/main.js
 */
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
