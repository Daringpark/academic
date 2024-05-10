<script setup>
import YoutubeCard from '@/components/YoutubeCard.vue'

import { ref } from 'vue'
import { useMovieStore } from '@/stores/counter'
const movieStore = useMovieStore()
// const movie = movieStore.searchReviews(20)

const whatIsearched = ref('')
const searchReviews = function () {
      if (whatIsearched.value.trim() != '') {
        console.log(whatIsearched.value)
      }
    }
</script>

<template>
  <main>
    <div class="text-center">
      <br>
      <h2>영화 리뷰 검색</h2>
      <!-- 아래 Form 추가 -->
      <!-- Form Input, submit, submit시 API 요청 화면 띄우기 -->
      <nav class="div">
        <form class="form d-flex justify-content-center" @submit.prevent="searchReviews">
          <input v-model="whatIsearched" class="form-control m-3 w-75" type="search" placeholder="영화 리뷰 검색..." aria-label="Search">
          <button class="btn btn-sm btn-outline-success m-3 w-25" type="submit">리뷰 검색</button>
        </form>
      </nav>
      <hr>
    </div>
    <!-- submit한 api 요청 이후, 카드 출력 -->
    <article>
      <YoutubeCard
      ></YoutubeCard>
    </article>
  </main>
  
</template>
