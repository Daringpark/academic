<script setup>
import { useProductStore } from '@/stores/products'
const store = useProductStore()



defineProps({
  product: Object
})
</script>

<template>
  <main>
    <div>
      <h4> {{ product.name }}</h4>
      <img :src="product.image" alt="">
      <div>￦ {{ product.price }}</div>
      <p v-show="!product.isFavorite"
      @click="store.favoriteToggle(product.name)">♡</p>
      <p v-show="product.isFavorite"
      @click="store.favoriteToggle(product.name)"
      class="red-heart">❤︎</p>
    </div>
  </main>
</template>

<style scoped>
main {
  border: 2px solid lightgray;
  margin: 16px;
  text-align: center;
}

img {
  width: 200px;
}

.red-heart {
  color: red;
}

div {
  margin: 8px;
}

</style>
