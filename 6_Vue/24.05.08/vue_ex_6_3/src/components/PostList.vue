

<template>
  <h3>{{ username }}이 작성한 글</h3>
  <hr>
  <PostListItem
  v-for="post in posts"
  :key="post.id"
  :my-post="post">
  </PostListItem>
  <hr>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import PostListItem from '@/components/PostListItem.vue'
import { useRoute, RouterLink, RouterView } from 'vue-router'

const route = useRoute()
const username = route.params.username

let id = 1
const posts = ref([
  { 'id': id++, title: 'Post1', content: 'Content1'}, 
  { 'id': id++, title: 'Post2', content: 'Content2'}, 
  { 'id': id++, title: 'Post3', content: 'Content3'}, 
])
</script>