


<template>
  <h2>
    [ TodoList ]
  </h2>
  <hr>
  <div>
    <ul>
      <TodoListItem
      v-for="todo in todos"
      :key="todo.id"
      :todo="todo"
      />
    </ul>
  </div>

</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue';

// 1. 변수를 import하고, 디렉토리 위치를 잘 작성한다.
import { useCounterStore } from '@/stores/counter'
// 객체를 변수 선언을 한다.
const store = useCounterStore()
const todos = store.todos
</script>