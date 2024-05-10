<script setup>
import MovieCard from '@/components/MovieCard.vue'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'

const movieStore = useMovieStore()

onMounted(() => {
  movieStore.getMovies()
  movieStore.getGenres()
})

</script>

<template>
  <main>
    <div class="text-center">
      <br>
      <h2 class="fw-bold">인기 순위 영화 목록</h2>
      <hr>
    </div>

    <div class="container">
      <div class="row d-flex justify-content-center">
        <MovieCard
        class="col-12 col-md-6 col-lg-4 col-xl-3 my-2"
        v-for="movie in movieStore.movieList"
        :key="movie.id"
        :movie="movie"
        />
      </div>
    </div>
    <!-- 아래 MovieCard -->
  </main>
</template>
