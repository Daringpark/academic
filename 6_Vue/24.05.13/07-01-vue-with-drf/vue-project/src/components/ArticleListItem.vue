<template>
  <div>
    <div>
      <h3>
        <span>
          {{ article.id }} |
        </span>
        <span>
          {{ article.title }}
        </span>
      </h3>
    </div>
    <div>
      {{ article.content }}
    </div>
    <RouterLink
    :to="{ name:'DetailView', params: { id: article.id}}">
      [TO ARTICLE DETAIL]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'


defineProps({
  article: Object
})



</script>

<style scoped>
div {
  margin: 8px;
}


</style>
