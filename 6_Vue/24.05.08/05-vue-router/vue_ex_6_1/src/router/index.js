import { createRouter, createWebHistory } from 'vue-router'


import Homeview from '@/views/Homeview.vue'
import About from '@/views/About.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [{
    // address
    path: '/',
    // name
    name: 'home',
    component: Homeview
  },
  {
    // address
    path: '/about',
    // name
    name: 'about',
    component: About
  }
  
  
  ]
})

export default router
