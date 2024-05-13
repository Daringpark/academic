import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {

  const posts = ref([])
  const BASE_API_URL = 'http://127.0.0.1:8000'

  const getPosts = function () {
    axios({
      method: 'get',
      url: `${BASE_API_URL}/api/v1/posts/`
    })
    .then((res) => {
      console.log(res)
      posts.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  return { posts, getPosts }
})
