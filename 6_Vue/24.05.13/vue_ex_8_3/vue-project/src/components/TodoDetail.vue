<template>
  <div>
    <h2>{{ todo.id }}번 째 할일</h2>
    <p>할 일 : {{ todo.work }}</p>
    <p>할 일 내용 : {{ todo.content }}</p>
    <p>완료 여부 : {{ todo.is_completed }}</p>
    <p>생성 일자 : {{ todo.created_at }}</p>
  </div>

</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  todo: Object
})
</script>
