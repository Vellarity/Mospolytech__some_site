<script setup>
import NavPanel from './components/NavPanel.vue';
import ShopView from './views/ShopView.vue';
import { RouterView } from 'vue-router';
import BackgroundImage  from "./components/atoms/BackgroundImage.vue"

import { useSessionStore } from "./storage/session"

const sessionStore = useSessionStore()

sessionStore.getSession()
console.log(sessionStore.csrf)
</script>

<template>
  <NavPanel />
  <div class="main flex flex-col flex-1">
    <RouterView />
  </div>
</template>

