<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">닉네임 : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>

      <div>
        <label for="password1">password : </label>
        <input type="password" id="password1" v-model.trim="password1">
      </div>

      <div>
        <label for="password2">password confirmation: </label>
        <input type="password" id="password2" v-model.trim="password2">
      </div>

      <input type="submit" value="회원가입">
    </form>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payload)
}


</script>

<style>

</style>
