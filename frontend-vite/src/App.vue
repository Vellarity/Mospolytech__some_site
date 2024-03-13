<script setup>
import NavPanel from './components/NavPanel.vue';
import { RouterView } from 'vue-router';
import { useSessionStore } from './storage/session';

const session = useSessionStore()

session.refreshSession()
</script>

<template>
  <NavPanel />
  <div class="main flex flex-col flex-1">
    <RouterView />
  </div>
</template>

