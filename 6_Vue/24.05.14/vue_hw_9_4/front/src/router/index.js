import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignupView from '@/components/SignupView.vue'
import LoginView from '@/components/LoginView.vue'
import { useArticleStore } from '@/stores/articles'

const router = createRouter({

  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.auth === null) {
          window.alert('로그인이 필요합니다.')
          return { name: 'login' }
        }
      }
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.auth !== null) {
          window.alert('이미 로그인 되어 있습니다.')
          return { name: 'home' }
        }
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.auth !== null) {
          window.alert('이미 로그인 되어 있습니다.')
          return { name: 'home' }
        }
      }
    },

  ]
})

export default router
