import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
// npm install pinia-plugin-persistedstate
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// npm install bootstrap@latest
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// import { library } from '@fortawesome/fontawesome-svg-core'
// import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// library.add(faUserSecret)

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
// app.component('F', FontAwesomeIcon)

app.use(pinia)
app.use(router)

app.mount('#app')
