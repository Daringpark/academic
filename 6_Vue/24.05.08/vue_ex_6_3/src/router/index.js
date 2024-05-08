import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import UserView from '../views/UserView.vue'
import Profile from '@/components/Profile.vue'
import Posts from '@/components/PostList.vue'
import ItemDetail from '@/components/PostDetail.vue'
import PostItem from '@/components/PostListItem.vue'

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
      path: '/user/:username',
      name: 'user',
      component: UserView,
      beforeEnter: (to) => {
        // username을 받는 걸 profile 페이지로 갈 곳의 params의 username으로
        const requestedUsername = to.params.username
        if (requestedUsername !== 'admin') {
          window.alert('현재 프로필 페이지는 admin만 접근 가능합니다.')
          return { name: 'home' }
        }
      },
      children: [
        { path: 'profile', name: 'user-profile', component: Profile},
        { path: 'posts',
          name: 'user-posts',
          component: Posts,
          children: [
            { path: `:id`, name: 'user-detail', component: ItemDetail}
          ]
        },
      ]
    },



  ]
})

export default router
