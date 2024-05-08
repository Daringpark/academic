<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink :to="{ name: 'some' }">SomeView</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name: 'other' }">OtherView</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name: 'students'}">Students</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
