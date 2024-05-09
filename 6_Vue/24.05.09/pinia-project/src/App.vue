<script setup>
import TodoList from '@/components/TodoList.vue';
import TodoForm from '@/TodoForm.vue';

import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
</script>

<template>
  <header>
    <div>
        <h1>
          [ TodoProject ]
        </h1>
      <hr>
      <hr>
        <TodoForm />
      <br>
      <hr>
        <div v-show="store.countDoneList">
          <span>
            <strong> ☆ 완료된 Todo: </strong> {{ store.countDoneList }}
          </span>
          <span v-show="store.countNotDoneList">
            <strong> ★ 미완료된 Todo: </strong> {{ store.countNotDoneList }}
          </span>
          <p v-show="!store.countNotDoneList">모든 일을 완료하셨습니다.</p>
        </div>
        <TodoList />
        </div>
  </header>

  <main>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

div {
  text-align: center;
}
</style>
