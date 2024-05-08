<script setup>
import businessCard from '@/components/BusinessCard.vue'

import { ref } from 'vue'
const businessCards = ref([
  { name: '일론 머스크', title:'테슬라 테크노킹'},
  { name: '래리 엘리슨', title:'오라클 창업주'},
  { name: '빌 게이츠', title:'마이크로소프트 공동창업주'},
  { name: '래리 페이지', title:'구글 공동창업주'},
  { name: '세르게이 브린', title:'구글 공동창업주'}
])

const deleteCardFunc = function (card) {
  businessCards.value = businessCards.value.filter(item => item !== card)
  console.log(businessCard.value)
}
</script>

<template>
  <div>
    <header>
      <h1>평함 관리 페이지</h1>
    </header>
  
    <main>
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      <article>
        <businessCard
        :cards="businessCards"
        @deleteCardFunc="deleteCardFunc"
        />
      </article>
    </main>
  
    <footer>
      <p>
        ⓒ 2024 My Business Cards Comperations
      </p>
    </footer>
  </div>

</template>

<style scoped>
div {
  margin: 16px;
  align-items: center;
  text-align: center;
}

header {
  border: 4px solid lightskyblue;
  background-color: lightblue;
  color: white;
  margin-left: 35%;
  margin-right: 35%;
}

footer {
  display: inline-block;
  background-color: lightgray;
  margin-top: 10%;
  width: 100%;
}
</style>
