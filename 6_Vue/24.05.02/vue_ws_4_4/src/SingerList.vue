<script setup>
import SingerDetail from '@/components/singers/singerDetail.vue'
</script>

<template>
  <h1>가수 목록</h1>
  <div>
    <SingerDetail />
    <SingerDetail />
    <SingerDetail />
    <SingerDetail />
  </div>
</template>

<style scoped>
.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
}

h1 {
  color: orange;
}
</style>
