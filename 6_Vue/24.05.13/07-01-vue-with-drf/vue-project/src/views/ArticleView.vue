<template>
  <div>
    <h1>Articles Page</h1>
    <RouterLink
    :to="{ name: 'CreateView'}"
    >
      [ Create ]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/ArticleList.vue'


const store = useCounterStore()
onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
