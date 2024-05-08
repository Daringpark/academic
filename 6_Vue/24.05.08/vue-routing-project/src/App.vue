<script setup>
import { RouterLink, RouterView } from 'vue-router'

import { ref } from 'vue'
const userid = ref(1)

</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink :to="{name : 'login'}">Login!</RouterLink>
        <RouterLink :to="{name : 'user', params: {'userid': userid}}">UserView</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
