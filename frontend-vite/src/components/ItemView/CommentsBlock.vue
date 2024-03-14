<script setup>
import Commentary from './Commentary.vue';
import CreateComment from './CreateComment.vue';

defineProps({
    comments:Array
})

</script>

<template>
    <div class="grid grid-cols-4 gap-4">
        <div class="bg-gray-100/75 backdrop-blur-sm col-span-3 rounded-2xl p-4 flex flex-col">
            <h2 class="font-semibold text-xl">Комментарии:</h2>
            <div class="flex flex-col flex-1">
                <Commentary v-if="comments?.length" v-for="comment of comments" :key="comment.id" v-bind="comment"/>
                <div v-else class="flex-1 flex justify-center items-center"><span>Комментариев нет</span></div>
            </div>
        </div>

        <CreateComment />
    </div>

</template>