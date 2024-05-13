
<template>
  <h3>할 일 상세 정보</h3>
  <hr>
  <div v-if="todo">
    <TodoDetail
    :todo="todo"
    >
    </TodoDetail>
  </div>

</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useTodoStore } from '@/stores/todoStore'
import axios from 'axios'

import TodoDetail from '@/components/TodoDetail.vue'

const store = useTodoStore()
const route = useRoute()

const todo = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.BASE_URL}/api/v1/todos/${route.params.id}/`
  })
  .then((res) => {
    console.log(res.data)
    todo.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
})


</script>


<style scoped>
</style>
