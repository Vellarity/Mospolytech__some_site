<script setup>
    import { ref } from 'vue'
    import {RouterLink} from "vue-router"

    import { useSessionStore } from '../storage/session';

    let isMenuOpened = ref(false);
    const sessionStore = useSessionStore()

</script>

<template>
    <nav class="w-full h-20 flex justify-center z-50">
        <div class="container backdrop-blur-sm rounded-b-2xl bg-gray-100/75 flex justify-between items-center p-4 relative h-20">
            <p></p>
            <span class="block h-full w-[32px] icon-menu" @click="isMenuOpened = !isMenuOpened"></span>

            <div v-if="isMenuOpened" class="backdrop-blur-sm rounded-2xl bg-gray-100 flex flex-col absolute right-0 py-2 px-2 w-52 top-20 gap-1 animate-menu-open">
                <div class="rounded-lg hover:bg-gray-300 cursor-pointer p-2 flex justify-end items-center gap-1">
                    <span class="icon icon-28 icon-profile"></span>
                    <router-link  v-if="!sessionStore.isAuthenticated" @click="isMenuOpened = !isMenuOpened" class="text-right text-lg font-medium" to="/login">Войти</router-link>
                    <router-link  v-else @click="isMenuOpened = !isMenuOpened" class="text-right text-lg font-medium" to="/profile">Профиль</router-link>
                </div>
                
                <div class="rounded-lg hover:bg-gray-300 cursor-pointer p-2 flex justify-end items-center gap-1">
                    <span class="icon icon-28 icon-profile"></span>
                    <router-link @click="isMenuOpened = !isMenuOpened" class="text-right text-lg font-medium" to="/">Магазин</router-link>
                </div>
            </div>
        </div>


        <!-- <NavMenu is-opened="{{ isMenuOpened }}"/> -->
    </nav>
</template>