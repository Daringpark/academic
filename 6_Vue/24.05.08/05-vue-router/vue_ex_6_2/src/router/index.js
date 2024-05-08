import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '@/views/UserView.vue'

const username = 'admin'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      // 동적 파라미터 적용 (Dynamic Params)
      path: '/user/:username',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from) => {
        if ( username !== 'admin') {
          alert('YOU ARE NOT ADMIN')
          return false
        }
      }
    },
  ]
})

export default router
