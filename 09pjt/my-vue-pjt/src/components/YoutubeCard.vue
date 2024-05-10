<script setup>
import { RouterLink } from 'vue-router'


const imgURL = (path, size = 300) => {
  // return `https://image.tmdb.org/t/p/w${size}${path}`
  return 1
}
</script>

<template>
  <main>
    <div class="text-center card">
      <!-- 썸네일 받아오기 -->
      <!-- <img class="card-img-left" :src="imgURL(movie.poster_path)" alt="movie_image"> -->
      <div class="card-body">
        <h4 class="card-title fw-bold"> 검색 기록 타이틀 </h4>
        <p class="card-text">
          검색 기록 내용
        </p>
      </div>
    </div>
  </main>
</template>
