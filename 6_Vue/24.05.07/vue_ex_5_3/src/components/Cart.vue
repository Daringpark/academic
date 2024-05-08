<template>
  <ul>
    <li v-for="cartitem in cart">
      <li>{{ cartitem.name }} - {{ cartitem.price }}원
          <button @click="removeToCart(cartitem)">물품 삭제!</button>
      </li>
    </li>
  </ul>
</template>

<script setup>
defineProps({
  cart: Array
})

const emit = defineEmits(['removeToCart'])
const removeToCart = function (cartitem) {
  emit('removeToCart', cartitem)
}
</script>
