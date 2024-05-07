<script setup>
import ParentChild from '@/components/ParentChild.vue'
import ParentItem from '@/components/ParentItem.vue'
import { ref } from 'vue'
const name = ref('Alice')
const fruits = ref([
  { id: 1, name: '사과'},
  { id: 2, name: '바나나'},
  { id: 3, name: '딸기'},
])
</script>

<template>
  <div>
    <ParentChild myprops="propsvalue" :dynamic-props="name"/>
    <!-- ParentChild로 "propsvalue"를 내려준다. -->
  </div>
    <ParentItem
      v-for="fruit in fruits"
      :key="fruit.id"
      :my-prop="fruit"
    />
  <div>
    
  </div>
</template>

<style scoped>

</style>