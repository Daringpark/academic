<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <!-- <button @click="addToCart">장바구니에 추가</button> -->
    <button @click="addToCart(product)">장바구니에 추가</button>
  </li>
</template>

<script setup>
const props = defineProps({
  product: Object
})

// 추가 버튼을 누르게 되면, 해당하는 데이터를 올려준다.
const emit = defineEmits(['addToCart'])
const addToCart = function (product) {
  // emit('addToCart', props.product)
  emit('addToCart', product)
}
</script>
