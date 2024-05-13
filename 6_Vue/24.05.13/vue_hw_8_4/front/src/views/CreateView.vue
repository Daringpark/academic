<template>
  <div>
    <h1>게시글 작성 페이지</h1>
    <hr>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content"> 내용 : </label>
      <input type="text" id="content" v-model.trim="content"><br>
      <input type="submit" value="게시글 작성!">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useArticleStore()

const title = ref(null)
const content = ref(null)
const createArticle = function () {
  store.createArticle(title, content)
  router.push({ name: 'HomeView' })
}

</script>

<style lang="scss" scoped>

</style>