import { createApp } from 'vue'
import App from './App.vue'
import MainPage from './pages/MainPage.vue'
import SetupPage from './pages/SetupPage.vue'

import axios from 'axios'
import VueAxios from 'vue-axios'

import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  { path: '/', component: MainPage },
  { path: '/setup', component: SetupPage }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

createApp(App)
  .use(VueAxios, axios)
  .use(router)
  .mount('#app')