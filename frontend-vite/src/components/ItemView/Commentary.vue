<script setup>
import { computed } from 'vue';
import Rating from '../atoms/Rating.vue';

const props = defineProps({
    user:Object,
    rate:Number,
    comment:String,
    author:String,
    date:String
})

const parsedDate = computed(() => {return new Date(props.date).toLocaleDateString()})

</script>

<template>
    <div class="w-full p-2 border-b border-b-gray-300 flex flex-col gap-1">
        <div class="flex gap-1">
            <span class="font-medium text-base">От:</span>
            <div v-if="user" class="font-medium text-base">{{user.username}} ({{user.fio || "Имя не указано"}})</div>
            <div v-else class="font-medium text-base">Неавторизованный пользователь ({{author ?? "Имя не указано"}})</div>
            <div class="ml-auto text-base font-medium">{{parsedDate}}</div>
        </div>
        <div class="flex gap-1 items-center">
            <span class="font-medium text-base">Оценка:</span>
            <Rating :active="false" :initial-rating="rate"/>
        </div>
        <div class="flex gap-1">
            <span class="font-medium text-base">Отзыв:</span>
            <p class="font-normal text-base">{{comment}}</p>
        </div>
    </div>
</template>