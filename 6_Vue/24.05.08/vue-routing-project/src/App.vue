<script setup>
import { RouterLink, RouterView } from 'vue-router'

import { ref } from 'vue'
const userid = ref(1)

</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink :to="{name : 'login'}">Login!</RouterLink>
        <RouterLink :to="{name : 'user', params: {'userid': userid}}">UserView</RouterLink>
      </nav>
    </div>

    <div>
      유희왕 듀얼몬스터즈 GX에서 유우키 쥬다이가 사용하는 엘리멘틀 히어로 중 하나. 쥬다이의 초창기 5개의 하급 엘리멘틀 히어로 중[1] 바람 속성을 담당한다.

작중에서는 1화의 크로노스 데 메디치와의 듀얼에서부터 가장 처음 선보인 몬스터로 등장. 성우는 히라노 타카히로/유동균. 주로 융합 소재로 사용되지만, 필드로 직접 나와 활약하는 경우도 꽤 있다. 만죠메 쥰과의 실기시험 듀얼을 포함해 여러 듀얼에서 피니시[2]를 날리기도 했다. 공격명은 '페더 브레이크(フェザー・ブレイク / Feather Break)', '페더 슬래시(Feather Slash)', '페더 플래시(Feather Flash)', '페더 슛(フェザー・シュート / Feather Shoot)'.[3] 여러 모션이 존재하는 상당히 버라이어티가 풍부한 기술이다.

사오토메 레이와의 듀얼에서는 사랑에 빠진 소녀의 효과로 인해 사랑에 빠져 엘리멘틀 히어로 스파크맨과 함께 쥬다이를 배신하는 추태를 보이기도 했다. 이후 엘리멘틀 히어로 버스트 레이디에게 혼쭐이 나면서 버스트 리턴의 효과로 패에 귀환, 엘리멘틀 히어로 프레임 윙맨의 융합 소재가 되었다.

여담으로 애니 초반의 카드 일러스트는 팔을 위로 뻗고 있는 모습이었다.

영문판의 이름인 'Avian'은 '새의, 조류의'라는 의미다.
    </div>
  </header>

  <RouterView />
</template>

<style>
@font-face {
    font-family: 'ONE-Mobile-Title';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/ONE-Mobile-Title.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}


@font-face {
    font-family: 'Eoe_Zno_EB';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_eight@1.0/Eoe_Zno_EB.woff') format('woff');
    font-weight: 700;
    font-style: normal;
}

/* div {
  font-family: Eoe_Zno_EB;
} */

div {
  font-family: ONE-Mobile-Title;
}
</style>
