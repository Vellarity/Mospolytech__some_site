<script setup>
import { ref } from 'vue';
import { localRoute } from "../../helper/constants"
import { RouterLink } from 'vue-router';

defineProps({
    shopItem:Object
})

</script>

<template>
    <RouterLink class="bg-gray-100/75 backdrop-blur-sm p-2 rounded-xl flex flex-col gap-1 cursor-pointer" :to="`/shop/${shopItem.id}`">
        <div class="bg-white rounded-lg w-full h-40">
            <img v-if="shopItem.image" alt="Нет изображения" class="h-40 w-full object-contain" :src="`${localRoute}/${shopItem.image}`" />
            <div v-else class="flex items-center h-full justify-center">
                Нет изображения
            </div>
        </div>
        <div class="text-lg font-semibold">{{shopItem.name}}</div>
        <template v-if="shopItem.size?.length">
            <div class="text-sm">Размеры</div>
            <div class="flex gap-1">
                <template v-for="size in shopItem.size">
                    <div
                        class="h-10 w-10 rounded-lg bg-gray-200 flex justify-center items-center font-medium text-sm"
                    >
                        {{size.name}}
                    </div>
                </template>
            </div>
        </template>
        <div v-else class="text-sm flex-1">
            Нет доступных размеров
        </div>
        <div class="flex justify-between items-center">
            <div class="text-lg font-semibold mt-2 p-2">
                {{shopItem.cost}} ₽
            </div>
        </div>
    </RouterLink>
</template>