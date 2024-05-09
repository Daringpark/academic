import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('counter', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
  ])

  // const matchName = computed(() => {
  //   const matchedName = route.params.name
  //   return balances.value.find(person => person.name === matchedName)
  // })
  
  const matchName = computed(() => {
    return (name) => balances.value.find(person => person.name === name)
  })


  const addBalance = function(name) {
    const matchedPerson = balances.value.find(person => person.name === name)
    matchedPerson.balance += 1000
  }


  return { balances, matchName, addBalance }
})
