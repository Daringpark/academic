<template>
  <ul>
    <ProductListItem 
      v-for="product in products" 
      :key="product.id" 
      :product="product"
      @add-to-cart="addToCart"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'
defineProps({
  products: Array,
})

// 최종 App으로 보내줄 정보를 emit 선언을 해준다.
const emit = defineEmits(['addToCart'])

const addToCart = function (product) {
  emit('addToCart', product)
}
</script>
