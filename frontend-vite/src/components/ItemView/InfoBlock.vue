<script setup>
import { defineProps } from 'vue';
import { localRoute } from '../../helper/constants';

defineProps({
    info:Object
})

</script>

<template>
    <div class="grid grid-cols-4 gap-4">
        <div class="col-span-1">
            <img v-if="info?.image" :src="`${localRoute}/${info?.image}`"/>
            <span v-else class="flex justify-center items-center">Нет изображения</span>
        </div>
    </div>
</template>