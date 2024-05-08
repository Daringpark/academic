
<script setup>
defineProps({
  childProp: Object,
})
const emit = defineEmits(['updateBalance'])

const giveAllowance = function () {
  emit('updateBalance')
}
</script>

<template>
  <body>
    <p style="margin-left: 16px;">
      <h3>자식 페이지입니다.</h3>
      <p>이름 : {{ childProp.name }}</p>
      <p>나이 : {{ childProp.age }}</p>
      <p>용돈 : {{ childProp.balance }}</p>
      <button @click="giveAllowance">{{ childProp.name }}에게 용돈을 주세요</button>
    </p>
  </body>
</template>

<style scoped>
body {
  border: 1px solid gray;
}
</style>