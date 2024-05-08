<template>
  <h1>UserHome</h1>




</template>

<script setup>
import { onBeforeRouteLeave } from 'vue-router';

// Route에서 나가기 전에 묻는 명령어
onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

</script>