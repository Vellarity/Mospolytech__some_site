<script setup>
import NavPanel from './components/NavPanel.vue';
import ShopView from './views/ShopView.vue';
import { RouterView } from 'vue-router';
import BackgroundImage  from "./components/atoms/BackgroundImage.vue"


</script>

<template>
  <NavPanel />
  <div class="main">
    <RouterView />
  </div>
</template>

