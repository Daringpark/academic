<template>
  <main class="container py-3">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <div class="col" v-for="number in numberOfItems">
        <GalleryListItem />
      </div>
    </div>
  </main>
</template>

<script setup>
import GalleryListItem from '@/components/GalleryListItem.vue';

import { ref } from 'vue'

const numberOfItems = ref(4)
</script>

<style scoped>

</style>
