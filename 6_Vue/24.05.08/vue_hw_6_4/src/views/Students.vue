
<template>
  <h1>Students Page</h1>
  <hr>
  <h2>학생 상세 정보 목록 입니다.</h2>
  <div v-for="student in students">
    <RouterLink
    :to="{ name: 'studentDetail', params: { name: student.name }}"
    >{{ student.name }} 학생 정보 보기</RouterLink>
  </div>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

const students = [
  {name: '김하나'},
  {name: '박두이'},
  {name: '이서이'},
]
</script>