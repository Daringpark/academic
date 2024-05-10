<script setup>
import MovieDetailInfo from '@/components/MovieDetailInfo.vue'
import { useMovieStore } from '@/stores/counter';
import { useRoute } from 'vue-router'
// movie.id는 알 수 있음
const route = useRoute()
const ID = route.params.movieId

const movieStore = useMovieStore()
const MovieDetail = movieStore.getMovieDetail(ID)
// console.log(MovieDetail)
</script>

<template>
  <main>
    <div class="text-center">
      <h3 class="fw-bold"> 영화 상세 페이지 </h3>
      <hr>
      <MovieDetailInfo
      :MovieDetail="MovieDetail"
      />
    </div>
  </main>
</template>


<style scoped>

</style>