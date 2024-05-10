<script setup>
import TrailerModal from '@/components/MovieTrailerModal.vue'
import { useMovieStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

// ID로 부터 movie불러오기
const route = useRoute()
const ID = route.params.movieId
const movieStore = useMovieStore()
const movie = movieStore.getMovieDetail(ID)

// movie로부터 장르 불러오기
const getGenre = movieStore.getGenre(movie.genre_ids)

defineProps({
  MovieDetail:Object
})

const imgURL = (path, size = 300) => {
  return `https://image.tmdb.org/t/p/w${size}${path}`
}

</script>

<template>
  <main>
      <div>
        <img :src="imgURL(MovieDetail.poster_path)" alt="Movie_image" class="mb-3">
        <h5 class="fw-bold">" {{ MovieDetail.title }} "</h5>
        <br>
        <div>
          <span class="fw-bold">개봉일 : </span>
          <span>{{ MovieDetail.release_date }}</span>
        </div>
        <div class="my-3">
          <span class="fw-bold">TMDB 평점: </span>
          <span>{{ MovieDetail.vote_average }}</span>
        </div>

        <div class="my-5">
          <h4 class="fw-bold"> 장르 </h4>
          <div v-for="genre in getGenre">
          - {{ genre.name }}
          </div>
        </div>
        <div>
          <h4 class="fw-bold my-3"> 줄거리 </h4>
          <div class="container">
            {{ MovieDetail.overview }}
          </div>
        </div>
        <div>
          <h4 class="fw-bold mt-4"> 공식 예고편 </h4>
          <button type="button" data-bs-toggle="modal" data-bs-target="#TrailerModal"
          class="btn btn-danger mt-3">유튜브 링크
          </button>
      
          <TrailerModal>   
          </TrailerModal>
        </div>
      </div>
  </main>
</template>
