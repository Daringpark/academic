<script setup>
const itemMsg = defineProps({
  myprops: String,
})
console.log(itemMsg)
console.log(itemMsg.myprops)
</script>

<template>
  <div>
    {{ myprops }}
  </div>
</template>

<style scoped>

</style>