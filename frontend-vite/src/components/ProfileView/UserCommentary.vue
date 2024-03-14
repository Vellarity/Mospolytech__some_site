<script setup>
import { computed } from "vue";
import Rating from "../atoms/Rating.vue"
import { RouterLink } from "vue-router";

const props = defineProps({
    rate:0,
    comment:"",
    wear:{},
    date:""
})

const parsedDate = computed(() => {return new Date(props.date).toLocaleDateString()})
</script>

<template>
    <div class="w-full p-2 border-b border-b-gray-300 flex flex-col gap-1">
        <div class="flex gap-1">
            <span class="font-medium text-base">Товар:</span>
            <RouterLink :to="`/shop/${props.wear.id}`" class="cursor-pointer font-medium">{{wear.name}}</RouterLink>
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