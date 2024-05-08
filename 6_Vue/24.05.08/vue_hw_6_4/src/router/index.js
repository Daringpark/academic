import { createRouter, createWebHistory } from 'vue-router'
import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'
import Students from '@/views/Students.vue'
import StudentDetail from '@/views/StudentDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'some',
      component: SomeView
    },
    {
      path:'/other',
      name:'other',
      component: OtherView
    },
    {
      path:'/students',
      name:'students',
      component: Students
    },
    {
      path:'/students/:name',
      name:'studentDetail',
      component: StudentDetail
    }
  ]
})

export default router
