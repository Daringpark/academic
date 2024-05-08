
<template>
  <h1>학생 상세 정보 페이지입니다.</h1>
  <hr>
  <p>
    이름 : {{ studentName }}
  </p>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const studentName = ref(route.params.name)


</script>