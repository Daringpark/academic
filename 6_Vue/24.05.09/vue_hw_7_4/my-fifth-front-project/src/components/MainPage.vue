

<template>
  <main>
    <div>이름 : {{ person.name }}</div>
    <div>잔고 : {{ person.balance }}</div>
    <button
    @click="updateBalance(person.name)">
    updateBalance
    </button>
  </main>
  <hr>
</template>

<script setup>
defineProps({
  person: Object 
})

import { useRoute, useRouter } from 'vue-router'
const router = useRouter()
const route = useRoute()


const updateBalance = function(name) {
  router.push({ name: 'update', params: {name: name} })
}
</script>


<style scoped>
main {
  margin-left: 8px;
}

div {
  margin-top: 16px;
}

button {
  margin-top: 20px;
  background-color: darkgreen;
  color: white;
}
</style>