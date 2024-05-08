
<template>
  <div>
    <span>{{ myPost.id }}. </span>
    <RouterLink :to="{ name: 'user-detail', params: { id: myPost.id }}">
      {{ myPost.title }}
    </RouterLink>
  </div>

</template>

<script setup>
import { RouterLink } from 'vue-router'

const props = defineProps(
  { myPost: Object }
)

</script>