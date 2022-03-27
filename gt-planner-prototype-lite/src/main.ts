import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import routes from 'virtual:generated-pages'
import { TroisJSVuePlugin } from 'troisjs'
import axios from 'axios'
import VueAxios from 'vue-axios'

import App from './App.vue'

import '@unocss/reset/tailwind.css'
import './styles/main.css'
import 'uno.css'

const app = createApp(App)
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
app.use(router)
app.use(VueAxios, axios)
app.use(TroisJSVuePlugin)
app.mount('#app')