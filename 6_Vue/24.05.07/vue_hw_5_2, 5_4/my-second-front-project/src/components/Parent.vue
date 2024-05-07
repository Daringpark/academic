
<script setup>
import chilldPage from '@/components/Child.vue'
import { ref } from 'vue'
const children = ref([
  { name: '김하나', age: 30, balance: 100000},
  { name: '김두리', age: 20, balance: 10000},
  { name: '김서이', age: 10, balance: 1000}
])
const updateBalance = function (child) {
  child.balance += 1000
}
</script>

<template>
  <body>
    <h1>부모 페이지입니다.</h1>
    <chilldPage
      v-for="child of children"
      :child-prop="child"
      @update-balance="updateBalance(child)"
    />
  </body>
</template>

<style scoped>
body {
  border: 1px solid gray;
}
h1 {
  margin-left: 16px;
}
</style>