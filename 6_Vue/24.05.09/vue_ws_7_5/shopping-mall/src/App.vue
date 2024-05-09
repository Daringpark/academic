<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useProductStore } from '@/stores/products';

const store = useProductStore()

</script>

<template>
  <header>
    <nav>
      <RouterLink
      :to="{ name: 'home' }"><h3>Home</h3></RouterLink>
      <RouterLink
      :to="{ name: 'products' }"><h3>Product</h3></RouterLink>
      <RouterLink
      :to="{ name: 'favorite' }">
      <div>
        <h3>Favorite</h3>
      </div>
      </RouterLink>
      <p v-show="store.favoriteCount">{{ store.favoriteCount }}</p>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
header {
  background-color: black;
  text-align: center;
}

nav {
  display: flex;
  justify-content: center;
}

h3 {
  color: white;
  margin-left: 8px;
  margin-right: 8px;
}

p {
  background: red;
  display: inline-block;
  border-radius: 50%;
  color: white;
  padding: 0px 8px;
}


</style>
