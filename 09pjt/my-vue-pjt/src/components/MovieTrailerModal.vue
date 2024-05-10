<script setup>
import { useMovieStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

// ID로 부터 movie불러오기
const route = useRoute()
const ID = route.params.movieId
const movieStore = useMovieStore()
const movie = movieStore.getMovieDetail(ID)

movieStore.getYoutube(ID)
const key = movieStore.YoutubeValue
// Youtube embed 띄워주기
const YoutubeURL = `http://www.youtube.com/embed/${key}`
</script>

<template>
  <main>
      <!-- modal -->
      <div class="modal fade" id="TrailerModal" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title fw-bold" id="exampleModalLabel">{{ movie.title }} 예고편</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <iframe :src="YoutubeURL" frameborder="0" width="100%" height="400">
              </iframe>
            </div>
            </div>
        </div>
      </div>

  </main>
</template>


<style scoped>

</style>