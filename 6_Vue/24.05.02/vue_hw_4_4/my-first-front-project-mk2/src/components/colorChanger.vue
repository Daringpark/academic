<script setup>
import { ref } from 'vue'

const colorClass = ref('')
</script>

<template>
  <input type="text" v-model="colorClass">
  <p :class="[colorClass]">입력창에 올바른 색상을 입력하면, 현재 문구의 색상이 변경됩니다!</p>
</template>

<style scoped>
.red {
  color: red;
}
.blue {
  color: blue;
}
.green {
  color: green;
}
</style>