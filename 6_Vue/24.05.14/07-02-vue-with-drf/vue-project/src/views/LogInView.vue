<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="Login">
      <div>
        <label for="username">닉네임 : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>

      <div>
        <label for="password">password : </label>
        <input type="password" id="password" v-model.trim="password">
      </div>

      <input type="submit" value="로그인">
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password = ref(null)


const Login = function () {

  const payload = {
    username: username.value,
    password: password.value
  }
  store.Login(payload)
}
</script>

<style>

</style>
