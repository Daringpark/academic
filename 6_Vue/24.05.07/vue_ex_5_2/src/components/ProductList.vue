<template>
  <li v-for="product in products" :key="product.id">
    <ProductListItem 
        :productName="product.name"
        :productPrice="product.price"
      />
  </li>
</template>

<script setup>
defineProps({
  products: Array
})
import ProductListItem from '@/components/ProductListItem.vue'
</script>
