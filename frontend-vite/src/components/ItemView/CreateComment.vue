<script setup>
import Rating from '../atoms/Rating.vue';
import { ref } from 'vue';

const fio = ref("")
const rating = ref(0)
const comment = ref("")
</script>

<template>
    <form id="create_comment" class="bg-gray-100/75 backdrop-blur-sm col-span-1 rounded-2xl p-4 h-fit flex flex-col gap-1">
        <h2 class="font-semibold text-xl">Оставить отзыв:</h2>
        <div class="flex flex-col gap-1">
            <template v-if="1">
                <div>
                    <label class="text-sm font-medium">ФИО (В свободной форме)</label>
                    <input
                        required
                        class="h-10 w-full p-1 rounded-lg border-2 border-gray-300 focus-visible:outline-gray-500 delay-150" 
                        name="fio" 
                        placeholder="Введите имя"
                    />
                </div>
            </template>
            <div>
                <label class="text-sm font-medium">Оценка</label>
                <Rating @update-rating="(i) => {rating = i}" :active="true"/>
            </div> 
            <div>
                <label class="text-sm font-medium">Отзыв</label>
                <textarea 
                    @input="$event => comment = $event.target.value"
                    class="w-full h-48 p-1 rounded-lg border-2 border-gray-300 focus-visible:outline-gray-500 delay-150 resize-none" 
                    name="commentary" 
                    placeholder="Введите текст"
                ></textarea>
            </div>               
        </div>
    </form>
</template>