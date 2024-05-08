
<template>
  <h3>제목 : {{ obj.title }} </h3>
  <p>번호 : {{ route.params.id }} </p>
  <p>내용 : {{ obj.content }} </p>
  
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router';
const route = useRoute()

let id = 1
const posts = ref([
  { id: id++, title: 'Post1', content: 'Content1'}, 
  { id: id++, title: 'Post2', content: 'Content2'}, 
  { id: id++, title: 'Post3', content: 'Content3'}, 
])

const obj = ref(posts.value[route.params.id - 1])
onBeforeRouteUpdate((to) => {
  obj.value = posts.value[to.params.id - 1]
  // console.log((posts.value.filter((post) => post.id == to.params.id))[0].title)
})

</script>