<script setup>
import ProfileInfoBlock from '../components/ProfileView/ProfileInfoBlock.vue';
import UserCommentary from '../components/ProfileView/UserCommentary.vue';
import { useUserStore } from '../storage/user';
import { watch } from 'vue';

const user = useUserStore()

watch(() => user.id, () => {
    user.getComments(user.id)
})

if (user.id)
    user.getComments(user.id)

</script>

<template>
    <div class="container gap-4 mx-auto grid grid-cols-profileBlock">
        <ProfileInfoBlock />

        <div class="bg-gray-100/75 backdrop-blur-sm p-4 rounded-2xl flex flex-col gap-4">
            <h2 class="font-semibold text-2xl">Мои отзывы</h2>
            <UserCommentary v-for="comment in user.comments" :key="comment.id" v-bind="comment"/>
        </div>
    </div>
</template>