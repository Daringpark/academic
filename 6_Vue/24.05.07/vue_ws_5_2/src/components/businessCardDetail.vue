<script setup>
const cardprops = defineProps({
  card: Object,
})

const emit = defineEmits(['deleteCardFunc'])
const deleteCardFunc = function (card) {
  emit('deleteCardFunc', card)
}
</script>

<template>
  <main>
    <h3>
      이름 : {{ card.name }}
    </h3>
    <div>
      ★ {{ card.title }}
    </div>
    <button @click="deleteCardFunc(card)">♠ 명함 삭제!</button>
  </main>
</template>

<style scoped>
main {
  border: 2px solid black;
  background-color: lightgray;
  margin-top: 16px;
  margin-left: 30%;
  margin-right: 30%;
}

div {
  margin: 16px
}
</style>
