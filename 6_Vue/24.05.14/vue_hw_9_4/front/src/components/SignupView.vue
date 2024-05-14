<template>
  <div>
    <h2>회원가입</h2>
    <div>
      <form @submit.prevent="fillForm">
        <div>
          <label for="username">아이디 : </label>
          <input type="text" id="username" v-model.trim="username">
        </div>
        <div>
          <label for="password">비밀번호 : </label>
          <input type="password" id="password" v-model.trim="password1">
        </div>
        <div>
          <label for="password_conf">비밀번호 확인 : </label>
          <input type="password" id="password_conf" v-model.trim="password2">
        </div>
        <input type="submit" value="회원가입">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const fillForm = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signup(payload)
}


</script>

<style lang="scss" scoped>

</style>