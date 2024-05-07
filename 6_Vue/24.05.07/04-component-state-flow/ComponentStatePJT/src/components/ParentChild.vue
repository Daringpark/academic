<script setup>
// 1. 문자열 배열을 사용하는 경우
// defineProps(['myprops'])

// 2. 객체를 사용하여 선언하는 경우
const msgConstant = defineProps({
  myprops: String,
  dynamicProps: String,
})
console.log(msgConstant)
console.log(msgConstant.myprops)

import ParentChildItem from '@/components/ParentChildItem.vue'
</script>

<template>
  <div>
    {{ myprops }}
    <ParentChildItem :myprops="myprops" />
  </div>
  <div>
    {{ dynamicProps }}
  </div>
</template>

<style scoped>

</style>