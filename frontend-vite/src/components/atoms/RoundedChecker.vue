<script setup>
    import { ref } from 'vue'
    import {useFiltersStore} from "../../storage/filters"

    defineProps({
        selectedColorBg: String,
        classNames: String,
        value: String,
    })

    let isChecked = ref(false)

    const filtersStore = useFiltersStore()
</script>

<template>
    <div @click="isChecked = !isChecked; filtersStore.updateQueryColor(isChecked, value)" :class="['rounded-full p-[2px] cursor-pointer', classNames, isChecked ? 'checked border-black border' : '']">
        <div :class="['rounded-full p-[1px] h-full w-full', selectedColorBg]"></div>
    </div>
</template>