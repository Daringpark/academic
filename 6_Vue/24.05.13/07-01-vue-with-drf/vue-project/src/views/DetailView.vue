<template>
  <div v-if="article" >
    <h3>{{ article.id }}</h3>
    <p>
      <h2>{{ article.title }}</h2>
      <p>
        글 내용 : {{ article.content }}
      </p>
      <p>
        Created at : {{ article.created_at }}
      </p>
      <p>
        Updated at : {{ article.updated_at }}
      </p>
    </p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method:'GET',
    url: `${store.API_URL}/api/v1/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})


</script>

<style>

</style>
