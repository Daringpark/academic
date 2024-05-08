<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
      <h1>Router 연습하기</h1>

      <nav>
        <RouterLink :to="{ name: 'some'}">Some</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name: 'other'}">Other</RouterLink>
      </nav>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style scoped>

</style>