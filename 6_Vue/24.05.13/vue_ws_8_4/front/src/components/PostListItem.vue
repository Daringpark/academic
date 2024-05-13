
<template>
  <main>
    <div>
      <h2>{{ post.id }}번째 글</h2>
      <h3>글 제목 : {{ post.title }}</h3>
      <p>글 내용 : {{ post.content }}</p>
      <hr>
    </div>

  </main>
</template>

<script setup>

defineProps({
  post:Object
})

</script>

<style scoped>

</style>