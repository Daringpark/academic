import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

const TOKEN = import.meta.env.VITE_TMDB_TOKEN_KEY
export const useMovieStore = defineStore('counter', () => {

  // 저장할 List state
  const movieList = ref([])
  const genreList = ref([])

  // 앱 실행시 MovieList를 받아올 Action
  const getMovies = function() {
    if (movieList) {
      axios({
        method: 'GET',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {language: 'ko-KR', page: '1'},
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${TOKEN}`
        }
      })
        .then((response) => {
          // console.log(response.data)
          movieList.value = response.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }

  const getGenres = function() {
    if (genreList) {
      axios({
        method: 'GET',
        url: 'https://api.themoviedb.org/3/genre/movie/list',
        params: {language: 'ko'},
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${TOKEN}`
        }
      })
        .then((response) => {
          // console.log(response.data.genres)
          genreList.value = response.data.genres
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }

  const getMovieDetail = function(ID) {
    return movieList.value.find((movie) => movie.id == ID)
  }

  const getGenre = function(genres) {
    const Value = genreList.value.filter((genre) => genres.includes(genre.id))
    return Value
  }

  const YoutubeValue = ref('')
  const getYoutube = function(ID) {
    axios({
      method: 'GET',
      url: `https://api.themoviedb.org/3/movie/${ID}/videos`,
      params: {language: 'ko-KR'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TOKEN}`
      }
    })
      .then((response) => {
        // console.log(response.data.results[0].key)
        YoutubeValue.value = response.data.results[0].key
      })
      .catch((err) => {
        console.log(err)
      })
  }



  return { movieList, genreList, YoutubeValue, getMovies, getGenres,
    getMovieDetail, getGenre, getYoutube}
}, { persist: true })
