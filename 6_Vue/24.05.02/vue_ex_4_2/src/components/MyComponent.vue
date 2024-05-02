<template>
  <div>

    <header class="row align-items-center">
      <h1>Gallery</h1>
    </header>

    <main class="container my-5">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
          <div class="card col" v-for="item in numberOfItem">
            <img src="@/assets/sample.png" alt="card_sample_img" style="width: 100%;">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
    </main>
    
  </div>
</template>

<script setup>
import { ref } from 'vue'
const numberOfItem = ref(4)

</script>

<style scoped>
div {
  text-align: center;
}

header {
  position: sticky;
  top: 0;
  z-index: 1;
  background-color: greenyellow;
  height: 100px;
}
</style>
