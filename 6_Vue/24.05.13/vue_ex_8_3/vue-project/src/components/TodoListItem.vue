<template>
  <div>
    <p>{{ todo.work}}</p>
    <p>{{ todo.content}}</p>
    <p>{{ todo.is_completed}}</p>
    <p>{{ todo.created_at}}</p>
  </div>
  <RouterLink
  :to="{ name:'DetailView', params: { id: todo.id} }"
  >할 일 상세보기</RouterLink>
  <hr/>
</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  todo: Object
})
</script>
