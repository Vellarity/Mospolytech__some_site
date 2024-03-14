<script setup>
import Rating from '../atoms/Rating.vue';
import { ref, nextTick } from 'vue';
import { localRoute } from '../../helper/constants';
import { useRoute } from 'vue-router';
import { useSessionStore } from '../../storage/session';
import { useUserStore } from '../../storage/user';
import { useItemStore } from '../../storage/item'

const route = useRoute()
const commentForm = ref(null)

const session = useSessionStore()
const item = useItemStore()

const wearID = route.params.itemID
const fio = ref("")
const rating = ref(1)
const comment = ref("")

const user = useUserStore()
user.getMe()

async function sendData(event) {
    if (!event) return 
    event.preventDefault()

    const formData = new FormData(event.target)

    try {
        let req = await fetch(event.target.action, {
            method:event.target.method,
            body:formData
        })
        if (!req.ok) return
        let res = await req.json()
        rating.value = 1
        comment.value = ""
        event.target.reset()
        await nextTick()
        await item.getComments(wearID)
    } catch (error) {
        console.error(error)
    }

}
</script>

<template>
    <form 
        ref="commentForm" 
        class="bg-gray-100/75 backdrop-blur-sm col-span-1 rounded-2xl p-4 h-fit flex flex-col gap-1"
        method="post"
        :action="localRoute + 'api/comments/'"
        @submit="(event) => sendData(event)"
    >
        <h2 class="font-semibold text-xl">Оставить отзыв:</h2>
        <input name="wear" class="hidden" :value="wearID"/>
        <div>
            <label class="text-base font-medium">Оценка</label>
            <input name="rate" :value="rating" class="hidden">
            <Rating @update-rating="(i) => {rating = i}" :initial-rating="rating" :active="true"/>
        </div> 
        <template v-if="!session.isAuthenticated">
            <div>
                <label class="text-base font-medium">ФИО (В свободной форме)</label>
                <input
                    required
                    @input="$event => fio = $event.target.value"
                    class="h-10 w-full p-1 rounded-lg border-2 border-gray-300 focus-visible:outline-gray-500 delay-150" 
                    name="author" 
                    placeholder="Введите имя"
                />
            </div>
        </template>
        <input v-else name="user" class="hidden" :value="user.id" >
        <div>
            <label class="text-base font-medium">Отзыв</label>
            <textarea 
                @input="$event => comment = $event.target.value"
                class="w-full h-48 p-1 rounded-lg border-2 border-gray-300 focus-visible:outline-gray-500 delay-150 resize-none" 
                name="comment" 
                placeholder="Введите текст"
            >{{comment}}</textarea>
        </div>               
        <button type="submit" class="bg-gray-300 p-2 rounded-lg">
            Отправить
        </button>
    </form>
</template>