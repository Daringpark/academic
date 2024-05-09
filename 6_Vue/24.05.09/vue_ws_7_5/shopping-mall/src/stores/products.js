import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('counter', () => {
  const productList = ref([
    {
      name: '상품 1',
      image: 'src/assets/product1.png',
      price: 100000,
      isFavorite: false
    },
    {
      name: '상품 2',
      image: 'src/assets/product2.png',
      price: 50000,
      isFavorite: false
    },
    {
      name: '상품 3',
      image: 'src/assets/product3.png',
      price: 1000,
      isFavorite: false
    },
    {
      name: '상품 4',
      image: 'src/assets/product4.png',
      price: 30000,
      isFavorite: false
    },
  ])

  const favoriteCount = computed(() => {
    return productList.value.filter((product) => product.isFavorite).length
  })

  const favoriteToggle = function(name) {
    const item = productList.value.find((product) => product.name === name)

    if (item.isFavorite === true) {
      item.isFavorite = false
    } else {
      favoriteList.value.push(item)
      item.isFavorite = true
    }
  }

  const favoriteList = computed(() => {
    return productList.value.filter((product) => product.isFavorite)
  })

  
  return { productList, favoriteCount, favoriteToggle, favoriteList }
}, {persist: true})
