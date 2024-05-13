<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <hr>
    <button>
      <RouterLink
      :to="{ name: 'CreateView'}">
        게시글 작성
      </RouterLink>
    </button>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { RouterLink } from 'vue-router'


</script>

<style lang="scss" scoped>

</style>