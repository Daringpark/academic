

<template>
  <h3> [상세 프로필] </h3>
  <p>안녕하세요. {{ username }} 입니다.</p>
</template>

<script setup>
import { useRoute } from 'vue-router'
const route = useRoute()
const username = route.params.username
</script>