<template>
  <div>
    {{ productName }} - {{ productPrice }}원
    <button>장바구니에 추가</button>
  </div>
</template>

<script setup>
defineProps({
  productName: String,
  productPrice: Int8Array,
})

</script>
