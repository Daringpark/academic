<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()
const goHome = function() {
  router.replace({ name: 'home' })
}
const userId = ref(route.params.userid)

import { onBeforeRouteUpdate } from 'vue-router';

const routeUpdate = function () {
  router.push({name: 'user', params: { userid: 100 }})
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.userid
})


</script>

<template>
  <div>
    <header>
      <h1>User View</h1>
      <h3>User Id : {{ userId }}</h3>
      <hr>
      <RouterLink :to="{ name: 'user-profile'}">Profile</RouterLink>
      <RouterLink :to="{ name: 'user-posts'}">Posts</RouterLink>
      <hr>
      <button @click="goHome">홈으로 !!</button>
      <button @click="routeUpdate">100번째 유저 페이지로</button>
    </header>

  </div>

  
  <RouterView/>
</template>
