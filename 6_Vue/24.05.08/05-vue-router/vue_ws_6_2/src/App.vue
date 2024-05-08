<template>
  <div class="quiz-app">
    <div class="app-header">
      <!-- 앱 이름 -->
      <h1>Quiz 퀴즈</h1>
    </div>
    <div class="app-description">
      <!-- 앱 설명 -->
      <p>여기는 퀴즈의 나라!</p>
    </div>
    <nav class="app-nav">
      <RouterLink :to="{ name:'home' }" class="nav-link">Home</RouterLink> | 
      <RouterLink :to="{ name:'quiz' }" class="nav-link">Quiz</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>

<script setuo>
import { RouterLink, RouterView } from 'vue-router';

</script>

<style scoped>
.quiz-app {
  background-color: lightgray;
  text-align: center;
  margin-left: 30%;
  margin-right: 30%;
}
.app-header {
  background-color: orange;
  color: white;
}

.app-nav {
  background-color: black;
  color: white;
}

.nav-link {
  color: white;
}
</style>
