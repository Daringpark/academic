<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <span v-if="!store.isAuthenticated"> | </span>
        <RouterLink :to="{ name:'signup' }" v-if="!store.isAuthenticated">회원가입</RouterLink>
        <span v-if="!store.isAuthenticated"> | </span>
        <RouterLink :to="{ name:'login' }" v-if="!store.isAuthenticated">로그인</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
