<script setup>
import { onMounted, ref, toValue } from 'vue';

defineProps({
    active:Boolean
})

defineEmits(["updateRating"])

const rating = ref(0)
const buttons = ref(null)

const activeClass = 'h-4 w-3 bg-gray-800 rounded-sm'
const noactiveClass = 'h-4 w-3 bg-gray-200 border border-gray-800 rounded-sm'

function changeRating(newRating) {
    rating.value = newRating
}

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
            ref="buttons"
        />
    </div>
</template>