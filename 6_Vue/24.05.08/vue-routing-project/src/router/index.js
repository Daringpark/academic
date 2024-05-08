import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserHome from '@/components/UserHome.vue'
import LoginView from '@/components/LoginView.vue'


const isAuthenticated = true

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
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      // pre-route Guard
      // 로그인 되어있다면, 로그인 View로 갈 수 없다.
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('로그인 상태입니다.')
          return { name: 'home' }
        }
      }
    },
    {
      path: '/user/:userid',
      component: UserView,
      children: [
        { path: '', name: 'user', component: UserHome},
        { path: 'profile', name: 'user-profile', component: UserProfile},
        { path: 'posts', name: 'user-posts', component: UserPosts},
      ]
    }
  ]
})

// // 전역 라우팅 가드
// router.beforeEach((to, from) => {
//   const isAuthenticated = false

//   // 아직 유효성 검사가 되지 않았기 때문에 + login외의 다른 곳으로 가려고 할 때
//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return { name: 'login'}
//   }
// })





export default router


