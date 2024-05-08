
<template>
  <header>
    <nav>
      <!-- Named Routing -->
      <RouterLink :to="{ name: 'home' }">Home</RouterLink> /
      <RouterLink :to="{ name: 'about' }">About</RouterLink>
    </nav>
  </header>

  <body>
    <!-- need to put RouterViewTag -->
    <RouterView />
  </body>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
