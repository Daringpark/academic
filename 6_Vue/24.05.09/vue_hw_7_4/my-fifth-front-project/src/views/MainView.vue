

<template>
  <div>
    <h3>메인 페이지</h3>
    <hr>
    <MainPage
    v-for="person in store.balances"
    :key="person.name"
    :person="person"
    />

  </div>

</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'
import MainPage from '@/components/MainPage.vue'
const store = useBalanceStore()
</script>