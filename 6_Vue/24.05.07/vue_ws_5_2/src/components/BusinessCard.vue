<script setup>
import businessCardDetail from '@/components/BusinessCardDetail.vue'

defineProps({
  cards: Array,
})
const emit = defineEmits(['deleteCardFunc'])
const deleteCardFunc = function (card) {
  emit('deleteCardFunc', card)
}
</script>

<template>
  <h3 v-show="cards != []"> 보유 명함 목록 </h3>
  <div v-for="card in cards">
      <businessCardDetail
      :card="card"
      @delete-Card-Func="deleteCardFunc"
      />
  </div>
</template>

<style scoped>
</style>
