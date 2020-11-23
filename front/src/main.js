// import Vue from 'vue'
import Vue from 'vue/dist/vue.esm.js'
// import App from './App.vue'
import Antd from 'ant-design-vue'
import VueRouter from 'vue-router'
import 'ant-design-vue/dist/antd.css'
import Home from '~/pages/Home'
import CaseList from '~/pages/CaseList'
import UrlsList from '~/pages/UrlsList'
import RunningResult from '~/pages/RunningResult'
import NavPage from '~/pages/NavPage'
import CaseSuit from '~/pages/CaseSuit'
import apiLogs from '~/pages/NavPage/apiLogs'
import navs from '@/components/Navigation'
Vue.config.productionTip = false
Vue.use(Antd)
Vue.use(VueRouter)
Vue.component('navs',navs)
const routes = [
  { path: '/caselist', component: CaseList },
  { path: '/', component: NavPage },
  { path: '/urls', component: UrlsList },
  { path: '/home', component: Home },
  { path: '/runningResult', name:'runningResult', component: RunningResult },
  { path: '/casesuite', component: CaseSuit },
  { path: '/Nav/apiLogs', name: 'apiLogs' , component: apiLogs}
]
const router = new VueRouter({
  routes,
  mode: 'hash',
})
new Vue({
  router,
  template: "<router-view></router-view>"
  // render: h => h(App),
}).$mount('#app')