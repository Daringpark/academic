<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>

<template>
  <header class="bg-dark text-white text-center">
    <div>
      <br>
      <h2 class="fw-bold">영화 추천 사이트</h2>
      <hr>
      <hr>
      <nav class="nav-bar">
        <RouterLink
        :to="{ name: 'home' }">
        <span class="text-white fw-bold">
          Home
        </span>
        </RouterLink>
      <span class="text-white"> | </span>
        <RouterLink
        :to="{ name: 'movieList' }">
        <span class="text-white fw-bold">
          영화 전체 리스트
        </span>
        </RouterLink>
      <span class="text-white"> | </span>
        <RouterLink
        :to="{ name: 'reviewSearch' }">
        <span class="text-white fw-bold">
          영화 리뷰 검색
        </span>
        </RouterLink>
      <span class="text-white"> | </span>
        <RouterLink
        :to="{ name: 'recommend' }">
        <span class="text-white fw-bold">
          오늘의 추천 영화
        </span>
        </RouterLink>
      </nav>
      <hr>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>



</style>
