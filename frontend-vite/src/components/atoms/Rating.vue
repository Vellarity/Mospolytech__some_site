<script setup>
import { onMounted, ref, toValue, watch } from 'vue';

const props = defineProps({
    active:Boolean,
    initialRating:Number
})

defineEmits(["updateRating"])

const rating = ref(props.initialRating ?? 1)

const activeClass = 'h-4 w-3 bg-gray-800 rounded-sm'
const noactiveClass = 'h-4 w-3 bg-gray-200 border border-gray-800 rounded-sm'

function changeRating(newRating) {
    if (props.active) rating.value = newRating
}

watch(() => props.initialRating, () => {
    if (props.active) rating.value = props.initialRating
})

</script>

<template>
    <div class="flex gap-1">
        <span 
            v-for="i of 5" 
            @click="() => {
                changeRating(i)
                $emit('updateRating', i)
            }"
            :key="i" 
            :class="[i<=rating ? activeClass : noactiveClass, 'cursor-pointer button_block']" 
        />
    </div>
</template>