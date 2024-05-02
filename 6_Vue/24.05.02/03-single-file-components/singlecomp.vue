<!-- template은 단 하나만 존재할 수 있다. -->
<template>

  <div>
    Hello!
  </div>

  <p class="greeting">
    {{ msg }}
  </p>
</template>

<!-- script setup 또한 하나만 존재할 수 있다. -->
<!-- 일반 script Tag는 올 수 있다. ex.) cdn불러오기, 새로운 script 작성 -->
<script setup>
import { ref } from 'vue'

const msg = ref('Hello!!!')
</script>

<!-- 여러 style Tag를 사용할 수 있음, style scoped는 현재 file의 template에만 적용한다. -->
<!-- scoped를 사용하지 않으면 전역으로 style이 적용된다. -->
<style scoped>
.greeting {
  color : crimson;
}
</style>