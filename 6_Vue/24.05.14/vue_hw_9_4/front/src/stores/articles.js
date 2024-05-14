import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const auth = ref(null)
  const isAuthenticated = ref(null)
  const token = ref(null)

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
    .catch((err) => {
      console.log(err)
    })
  }
  
  const createArticle = function ({ title, content }) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/articles/`,
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      console.log(res)
      router.push({name : 'home'})
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const signup = function (data) {
    const { username, password1, password2 } = data
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
    .then((res) => {
      const password = password1
      login({username, password})
    })
    .catch((err) => {
      if (err.message === 'Request failed with status code 400') {
        window.alert('이미 있는 계정입니다.')
      }
    })
  }

  const login = function (data) {
    const { username, password } = data
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then((res) => {
      token.value = res.data.key
      isAuthenticated.value = true
      auth.value = {isAuthenticated: isAuthenticated.value, token: token.value}
      router.push({name : 'home'})
    })
    .catch((err) => {
      console.log(err)
    })
  }


  return { articles, API_URL, auth, token, isAuthenticated, getArticles, createArticle, signup, login }
}, {persist : true})
