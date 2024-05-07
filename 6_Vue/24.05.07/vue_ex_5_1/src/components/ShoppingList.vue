
<script setup>
const productProp = defineProps({
  productProp: Object,
})

</script>

<template>
  <li>
    <div> {{ productProp.productProp.name }} - {{ productProp.productProp.price }}원 </div>
  </li>
</template>
