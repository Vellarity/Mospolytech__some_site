<script setup>
import { computed } from "vue";
import Rating from "../atoms/Rating.vue"
import { RouterLink } from "vue-router";
import { ref } from "vue";
import { localRoute } from "../../helper/constants";
import { useSessionStore } from "../../storage/session";

const props = defineProps({
    id:undefined,
    rate:0,
    comment:"",
    wear:{},
    date:""
})

const session = useSessionStore()

let isEdit = ref(false)

let oldValues = ref({
    rate: props.rate,
    comment:props.comment
})

let newValues = ref({
    id:props.id,
    rate: props.rate,
    comment:props.comment
})

const parsedDate = computed(() => {return new Date(props.date).toLocaleDateString()})

function changeIsEdit() {
    isEdit.value = !isEdit.value

    newValues.value.comment = oldValues.value.comment
    newValues.value.rate = oldValues.value.rate
}

async function saveData(){
    try {
        await session.refreshSession()
        let req = await fetch(`${localRoute}api/comments/${props.id}/`, {
            method:"PATCH",
            headers:{
                "Authorization":`Bearer ${localStorage.getItem("ACCESS_TOKEN")}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newValues.value)
        })
        if (!req.ok) {
            changeIsEdit()
            return
        }
        let res = await req.json()
        oldValues.value.comment = res.comment
        oldValues.value.rate = res.rate
        changeIsEdit()
    } catch (error) {
        changeIsEdit()
        console.log(error)
    }
}

</script>

<template>
    <div class="w-full p-2 border-b border-b-gray-300 flex flex-col gap-1">
        <div class="flex gap-1">
            <span class="font-medium text-base">Товар:</span>
            <RouterLink :to="`/shop/${props.wear.id}`" class="cursor-pointer font-medium">{{wear.name}}</RouterLink>
            <span @click="changeIsEdit()" class="icon icon-20 icon-square-pen"></span>
            <div class="ml-auto text-base font-medium">{{parsedDate}}</div>
        </div>
        <div class="flex gap-1 items-center">
            <span class="font-medium text-base">Оценка:</span>
            <Rating :active="isEdit" @update-rating="(i) => newValues.rate = i" :initial-rating="newValues.rate"/>
        </div>
        <div class="flex gap-1">
            <span class="font-medium text-base">Отзыв:</span>
            <p v-if="!isEdit" class="font-normal text-base">{{newValues.comment}}</p>
            <textarea 
                v-else
                @input="$event => newValues.comment = $event.target.value"
                class="w-full h-24 p-1 rounded-lg border-2 border-gray-300 focus-visible:outline-gray-500 delay-150 resize-none" 
                name="comment" 
                placeholder="Введите текст"
            >{{newValues.comment}}</textarea>
        </div>
        <div v-if="isEdit" class="flex justify-end">
            <button @click="saveData()" class="basic_button">Сохранить</button>
        </div>
    </div>
</template>