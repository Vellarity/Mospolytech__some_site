<script setup>

defineProps({
    user:Object,
    rate:Number,
    comment:String
})

</script>

<template>
    <div class="w-full p-2 border-b border-b-gray-300 flex flex-col gap-1">
        <div class="flex gap-1">
            <span class="font-medium text-base">От:</span>
            <div v-if="user">{{user.name}} {{user.fio}}</div>
            <div v-else class="font-medium text-base">Неавторизованный пользователь</div>
        </div>
        <div class="flex gap-1 items-center">
            <span class="font-medium text-base">Оценка:</span>
            <template v-for="i of 5">
                <span v-if="i <= rate" class="h-4 w-3 bg-gray-800 rounded-sm" />
                <span v-else class="h-4 w-3 bg-gray-200 border border-gray-800 rounded-sm" />
            </template>
        </div>
        <div class="flex gap-1">
            <span class="font-medium text-base">Отзыв:</span>
            <p>{{comment}}</p>
        </div>
    </div>
</template>