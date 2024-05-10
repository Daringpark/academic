<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  movie:Object
})

const imgURL = (path, size = 300) => {
  return `https://image.tmdb.org/t/p/w${size}${path}`
}
</script>

<template>
  <main>
    <div class="text-center card">
      <img class="card-img-top" :src="imgURL(movie.poster_path)" alt="movie_image">
      <div class="card-body">
        <h4 class="card-title fw-bold"> {{ movie.title }} </h4>
        <!-- <p class="card-text">
          {{ movie.overview }}
        </p> -->
        <RouterLink :to="{ name: 'movieDetail', params: { movieId: movie.id } }" class="btn btn-dark btn-sm">영화 세부정보 보기</RouterLink>
      </div>
    </div>
  </main>
</template>
