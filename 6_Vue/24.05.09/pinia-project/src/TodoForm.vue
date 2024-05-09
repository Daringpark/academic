


<template>
  <h2>
    ★ TodoForm ★
  </h2>
  <hr>
  <br>
  <div>
    <form @submit.prevent="createTodo(todoText)" ref="formText">
      <input type="text" v-model="todoText">
      <input type="submit" value=" 할 일 추가하기!">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

// 초기 입력할 위치의 값을 null로 준다.
const formText = ref(null)

const todoText = ref('')
const store = useCounterStore()

const createTodo = function (todoText) {
  // Todo를 추가하고
  store.addTodo(todoText)
  // 입력창의 Text value도 reset() -> null값으로 바꿔줘야한다.
  formText.value.reset()
}

</script>

<style scoped>
input {
  margin-left: 8px;
}
</style>