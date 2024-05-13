
<template>
  <main>
    <div>
      <h2>게시글 목록 페이지</h2>
    </div>
    <hr>
    <PostList
    :posts="store.posts"
    ></PostList>
  </main>
</template>

<script setup>
import PostList from '@/components/PostList.vue'

import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
onMounted(() => {
  store.getPosts()
})



</script>

<style scoped>

</style>