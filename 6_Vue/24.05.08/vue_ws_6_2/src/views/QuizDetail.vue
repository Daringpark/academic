<template>
  <div class="main-page">
    <!-- 화면 구성 -->
    <h4 class="body">
      <span>
        {{ myQuiz.pk }}번 문제! {{ myQuiz.question }}
      </span>
    </h4>
    <hr>
    <div>
      <h4>※ 정답 입력 ※</h4>
      <input type="text">
    </div>
  </div>
</template>

<script setup>
defineProps({
  myQuiz : Object
})

</script>

<style scoped>
.main-page {
  background-color: lightgray;
  margin: 16px;
  margin-left: 30%;
  margin-right: 30%;
}

.body {
  text-align: center;
  margin: 16px;
}

div {
  background-color: whitesmoke;
  text-align: center;

}
</style>
