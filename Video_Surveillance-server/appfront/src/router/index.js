import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import login from '@/components/login'
import cache from '@/components/cache'
import client_config from '@/components/client_config'
import close_restaurant from '@/components/close_restaurant'
import open_restaurant from '@/components/open_restaurant'
import restaurant_list from '@/components/restaurant_list'
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'home',
      component: home,
      meta: {
        title: '算法配置'
      }
    },
    {
      path: '/',
      name: 'login',
      component: login,
      meta: {
        title: '登录'
      }
    },
    {
      path: '/cache',
      name: 'cache',
      component: cache,
      meta: {
        title: '缓存设置'
      }
    },
    {
      path: '/client_config',
      name: 'client_config',
      component: client_config,
      meta: {
        title: 'Client算法配置'
      }
    },
    {
      path: '/close_restaurant',
      name: 'close_restaurant',
      component: close_restaurant,
      meta: {
        title: '关店设置'
      }
    },
    {
      path: '/open_restaurant',
      name: 'open_restaurant',
      component: open_restaurant,
      meta: {
        title: 'Client在线检测'
      }
    },
    {
      path: '/restaurant_list',
      name: 'restaurant_list',
      component: restaurant_list,
      meta: {
        title: 'ID列表刷新'
      }
    },
  ]
})
