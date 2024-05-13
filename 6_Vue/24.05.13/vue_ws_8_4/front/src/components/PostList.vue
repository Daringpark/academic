
<template>
  <main>
    <PostListItem
    v-for="post in posts"
    :key="post.id"
    :post="post"
    >
    </PostListItem>
  </main>
</template>

<script setup>
import PostListItem from '@/components/PostListItem.vue'

defineProps({
  posts:Object
})

</script>

<style scoped>

</style>