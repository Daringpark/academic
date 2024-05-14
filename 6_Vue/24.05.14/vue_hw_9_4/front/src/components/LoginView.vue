<template>
  <div>
    <h2>로그인 페이지</h2>
    <div>
      <form @submit.prevent="fillForm">
        <div>
          <label for="username">아이디 : </label>
          <input type="text" id="username" v-model.trim="username">
        </div>
        <div>
          <label for="password">비밀번호 : </label>
          <input type="password" id="password" v-model.trim="password">
        </div>
        <input type="submit" value="로그인">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

const username = ref(null)
const password = ref(null)

const fillForm = function() {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.login(payload)
}


</script>

<style lang="scss" scoped>

</style>