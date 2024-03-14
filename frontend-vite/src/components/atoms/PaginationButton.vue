<script setup>

const props = defineProps({
    value:String,
    link:String,
    isActive:Boolean
})

</script>

<template>
    <div :class="['h-10 w-10 rounded-lg border-gray-300 border flex justify-center items-center cursor-pointer', isActive ? 'bg-gray-300' : 'bg-gray-100/75']">
        <span class="font-medium">{{value}}</span>
    </div>
</template>