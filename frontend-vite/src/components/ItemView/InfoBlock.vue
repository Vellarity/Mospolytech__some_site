<script setup>
import { defineProps } from 'vue';
import { localRoute } from '../../helper/constants';

defineProps({
    info:Object
})

</script>

<template>
    <div class="grid grid-cols-4 gap-4 h-80">

        <div class="col-span-1 flex justify-center bg-gray-100/75 backdrop-blur-sm rounded-2xl p-4 h-80">
            <img v-if="info?.image" class="max-w-full object-contain" :src="`${localRoute}/${info?.image}`"/>
            <span v-else class="flex justify-center items-center bg-gray-100/75 backdrop-blur-sm h-full rounded-2xl">Нет изображения</span>
        </div>

        <div class="col-span-1 bg-gray-100/75 backdrop-blur-sm h-full rounded-2xl flex flex-col gap-2 p-4">
            <h3 class="text-xl font-semibold col-start-1 col-end-3">Коротко о товаре:</h3>
            <div class="flex gap-1 items-baseline">
                <span class="font-medium text-lg">Название:</span>
                <span>{{info.name}}</span>
            </div>
            <div class="flex gap-1 items-baseline">
                <span class="font-medium text-lg">Цвет:</span>
                <span>{{info.color}}</span>
            </div>
            <div class="flex gap-1 items-baseline">
                <span class="font-medium text-lg">Тип:</span>
                <span>{{info.type}}</span>
            </div>
            <div class="flex gap-1 items-baseline">
                <span class="font-medium text-lg">Цена:</span>
                <span>{{info.cost}} ₽</span>
            </div>
            <div class="flex gap-1 items-baseline">
                <span class="font-medium text-lg">Доступные размеры:</span>
            </div>
            <div class="flex gap-1">
                <template v-if="info.size?.length" v-for="size in info.size">
                    <div
                        class="h-10 w-10 rounded-lg bg-gray-200 flex justify-center items-center font-medium text-sm"
                    >
                        {{size.name}}
                    </div>
                </template>
                <div v-else>
                    Нет доступных размеров
                </div>
            </div>
        </div>

        <div class="col-span-2 bg-gray-100/75 backdrop-blur-sm h-full rounded-2xl flex flex-col gap-2 p-4">
            <h3 class="text-xl font-semibold col-start-1 col-end-3">Описание:</h3>
            <p class="text-base">
                {{info.infoText}}
            </p>
        </div>
    </div>
</template>