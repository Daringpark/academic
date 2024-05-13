<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink
      :to="{ name : 'MainView'}">
      <span>Home</span>
      </RouterLink>
      <span> | </span>
      <RouterLink
      :to="{ name : 'PostListView'}">
      <span>PostList</span>
      </RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  background-color: black;
  text-align: center;
}

span {
  color: white;
}
</style>
