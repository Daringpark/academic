<script setup>
import { useProductStore } from '@/stores/products'
const store = useProductStore()
const products = store.productList

import ProductDetail from '@/components/ProductDetail.vue'

</script>

<template>
  <main>
    <h1>상품 페이지</h1>
    <div class="container">
      <ProductDetail
      v-for="product in products"
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
