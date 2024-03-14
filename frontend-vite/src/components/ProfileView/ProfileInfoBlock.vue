<script setup>
import { useUserStore } from '../../storage/user';
import { ref } from 'vue';

const user = useUserStore()
user.getMe().then((res) => {
    newdata.value = res
})

let isEdit = ref(false)

let newdata = ref({
    id:user.id,
    username:user.username,
    profile:{
        fio:user.profile.fio,
        email:user.profile.email,
        number:user.profile.number,
        geo:user.profile.geo
    }
})

</script>


<template>
    <div class="bg-gray-100/75 backdrop-blur-sm p-4 rounded-2xl flex flex-col gap-4 h-min">
        <div class="flex justify-between items-end">
            <h2 class="font-semibold text-2xl">Информация о пользователе</h2>
            <span @click="isEdit=!isEdit" class="icon icon-28 icon-square-pen"></span>
        </div>

        <div class="grid gap-4">
            <div class="flex flex-col gap-1">
                <label class="font-semibold text-xl">Имя профиля</label>
                <div v-if="!isEdit" class="text-lg">{{user.username}}</div>
                <input v-else @input="(e) => {newdata.username = e.target.value}" name="username" placeholder="username" class="basic_input" :value="newdata.username">
            </div>
            <div class="flex flex-col gap-1">
                <label class="font-semibold text-xl">Имя (В свободной форме)</label>
                <div v-if="!isEdit" class="text-lg">{{user.profile.fio || "Не задано"}}</div>
                <input v-else @input="(e) => {newdata.profile.fio = e.target.value}" name="fio" placeholder="Иванов Иван" class="basic_input" :value="newdata.profile.fio">
            </div>
            <div class="flex flex-col gap-1">
                <label class="font-semibold text-xl">Почта</label>
                <div v-if="!isEdit" class="text-lg">{{user.profile.email || "Не задано"}}</div>
                <input v-else @input="(e) => {newdata.profile.email = e.target.value}" name="email" type="email" placeholder="example@mail.com" class="basic_input" :value="newdata.profile.email">
            </div>
            <div class="flex flex-col gap-1">
                <label class="font-semibold text-xl">Номер телефона</label>
                <div v-if="!isEdit" class="text-lg">{{user.profile.number || "Не задано"}}</div>
                <input v-else @input="(e) => {newdata.profile.number = e.target.value}" name="number" type="text" placeholder="+7 (999) 999-99-99" class="basic_input" :value="newdata.profile.number">
            </div>
            <div class="flex flex-col gap-1">
                <label class="font-semibold text-xl">Адрес</label>
                <div v-if="!isEdit" class="text-lg">{{user.profile.geo || "Не задано"}}</div>
                <input v-else @input="(e) => {newdata.profile.geo = e.target.value}" name="geo" placeholder="г.Москва, ул.Пушкина, д.4" class="basic_input" :value="newdata.profile.geo">
            </div>
            <div v-if="isEdit" class="flex flex-col gap-1">
                <button @click="() => {user.updateData(newdata); isEdit = !isEdit}" class="basic_button">Сохранить изменения</button>
            </div>
        </div>
    </div>
</template>