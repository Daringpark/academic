<template>
  <div>
    <div>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
    </div>
  </div>
  <hr>
</template>

<script setup>
defineProps({
  article: Object
})


</script>

<style lang="scss" scoped>

</style>