import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // ref == state
  const id = ref(0)
  const todos = ref([])

  // computed == getters
  const countDoneList = computed(() => {
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })

  const countNotDoneList = computed(() => {
    const realTodos = todos.value.filter((todo) => !todo.isDone)
    return realTodos.length
  })
  
  // function == action
  // C of CRUD
  const addTodo = function(todoText) {
    todos.value.push({
      id: id.value++,
      text: todoText,
      isDone: false
    })
    console.log(todoText)
  }
  
  // D of CRUD
  const deleteTodo = function (todoId) {
    // Index를 받아온다.
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    // splice를 사용해서 해당 index를 삭제
    todos.value.splice(index, 1)
  }
  
  // U of CRUD
  const updateTodo = function (todoId) {
    todos.value = todos.value.map((todo) =>{
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }



  // plugin == npm 외부 설치를 통해서 불러오는 경우에 사용할 수 있다.


  // 어디에서든 사용하게 하려면, return을 한다. 공유하지 않는 속성을 counter.js에 작성할 필요없다.
  return { id, todos, addTodo, deleteTodo, updateTodo, countDoneList, countNotDoneList }
}, { persist: true})