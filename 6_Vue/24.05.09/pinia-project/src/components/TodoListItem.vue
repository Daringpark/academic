
<template>
  <div>
    <li>
      <input type="checkbox" @click="store.updateTodo(todo.id)" name="updateCheckBox">
      <!-- todo 내용을 눌렀을 경우, linethrough 되는 css를 True로 만들어준다. -->
      <span :class="{ 'is-done': todo.isDone }">
        {{ todo.text }}
      </span>
      <button @click="store.deleteTodo(todo.id)">Delete</button>
    </li>
  </div>

</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()

// todoItem은 todo객체를 하나씩 받는다.
// 어디에서? TodoList에서 props로 보낸 값을 :todo="todo"
// 왼쪽은 하위에서 사용할 이름, 오른쪽은 상위에서 보낼 것
defineProps({
  todo: Object
})

</script>

<style scoped>
button {
  margin-left: 8px;
  margin-top: 8px;
}

div {
  display: flex;
  justify-content: center;
  text-align: left;
}

.is-done {
  text-decoration: line-through;
}

</style>