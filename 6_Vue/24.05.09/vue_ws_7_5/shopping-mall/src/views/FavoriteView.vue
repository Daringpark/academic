<script setup>
import { useProductStore } from '@/stores/products';
const store = useProductStore()

import ProductDetail from '@/components/ProductDetail.vue'
</script>

<template>
  <main>
    <h1>장바구니 페이지</h1>
    <div>
      <ProductDetail
      v-for="product in store.favoriteList"
      :key="product.name"
      :product="product"
      />
    </div>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1 {
  margin-top: 64px;
}

</style>
