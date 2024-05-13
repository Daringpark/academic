import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {

  // const articles = ref([
  //   { id: 1, title: '제목1', content: '내용1'},
  //   { id: 2, title: '제목2', content: '내용2'},
  // ])

    const articles = ref([])
    const API_URL = 'http://127.0.0.1:8000'

    const getArticles = function () {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/`
      })
        .then((response) => {
          // console.log(response.data)
          articles.value = response.data
        })
        .catch((err) => {
          console.log(err)
        })
    }


  return { API_URL, articles, getArticles, }
}, { persist: true })
