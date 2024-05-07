<script setup>
defineProps({
  myProp: Object,
})
</script>

<template>
  <div>
    <p>{{ myProp.id }} || {{ myProp.name }}</p>
  </div>
</template>

<style scoped>

</style>