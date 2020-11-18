/*
 * @Author       : Wang.HH
 * @Date         : 2020-10-22 14:20:18
 * @LastEditTime : 2020-10-29 13:50:13
 * @LastEditors  : Wang.HH
 * @Description  : your description
 * @FilePath     : /My-VUE-Python/Vue/element-ui/src/router/index.js
 */
import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import FirstPage from '../pages/1.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'FirstPage',
      component: FirstPage
    },
    {
      path: '/3333',
      name: 'ThirdPage',
      component: () => import('../pages/2/3.vue')
    },
    {
      path: '/2222',
      name: 'SecondPage',
      component: () => import('../pages/2/2.vue'),
      children: [
        {
          path: '3333',
          name: 'ThirdPage',
          component: () => import('../pages/2/3.vue')
        }
      ]
    }
  ]
})
