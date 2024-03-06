<script setup>
import ProfileInfoBlock from '../components/ProfileView/ProfileInfoBlock.vue';


</script>

<template>
    <div class="container gap-4 mx-auto grid grid-cols-profileBlock">
        <ProfileInfoBlock />

        <div class="bg-gray-100 p-4 rounded-2xl flex flex-col gap-4">
            <h2 class="font-semibold text-2xl">История заказов</h2>


        </div>
    </div>
</template>