<script setup>
import { useSessionStore } from '../storage/session';
import { localRoute } from '../helper/constants';

async function loginOrRegister(e) {
    if (!e) return
    e.preventDefault()
    console.log(e.target)

    let formData = new FormData(e.target)
    try {
        let req = await fetch(e.target.action, {
            method:e.target.method,
            body:formData,
            credentials: "include",
            headers:{
                "X-CSRFToken":localStorage.get("csrftoken"),
            }
        })
        let res = await req.json()
        console.log(res)
    } catch (error) {
        console.error(error)
    }
}

</script>

<template>
    <div class="container m-auto flex flex-col items-center justify-center gap-4">
        <form method="post" class="w-96 rounded-2xl p-4 bg-gray-100/75 backdrop-blur-sm flex flex-col gap-4 items-center">
            <h2 class="font-semibold text-xl">Авторизация</h2>
            <div class="flex flex-col w-full">
                <label for="username" class="font-medium">Имя пользователя</label>
                <input name="username" class="basic_input">
            </div>
            <div class="flex flex-col w-full">
                <label for="password" class="font-medium">Пароль</label>
                <input type="password" name="password" class="basic_input">
            </div>
            <div class="flex gap-4 w-full">
                <button @submit="(e) => {loginOrRegister(e)}" :formaction="`${localRoute}api/auth/register/`" type="submit" class="basic_button text-base flex-1">Регистрация</button>
                <button @submit="(e) => {loginOrRegister(e)}" :formaction="`${localRoute}api/auth/login/`" type="submit" class="basic_button text-base flex-1">Вход</button>
            </div>
        </form>
    </div>
</template>