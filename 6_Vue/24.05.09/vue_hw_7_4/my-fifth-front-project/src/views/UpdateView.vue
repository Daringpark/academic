

<template>
  <div>
    <h3>데이터 수정 페이지</h3>
    <hr>
    <p>이름 : {{ name }}</p>
    <p>잔고 : {{ matchedPerson.balance }}</p>
    <button
    @click="addBalance(name)">
      * 잔고에 1000원 입금하기 *
    </button>
  </div>

</template>

<script setup>
import { useRoute } from 'vue-router'

import { useBalanceStore } from '@/stores/balance'

const store = useBalanceStore()
const route = useRoute()

const name = route.params.name
const matchedPerson = store.matchName(name)
console.log()
const addBalance = store.addBalance

</script>

<style scoped>
p {
  margin-left: 8px;
}
</style>