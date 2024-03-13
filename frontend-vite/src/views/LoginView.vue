<script setup>
import { useSessionStore } from '../storage/session';
import { localRoute } from '../helper/constants';
import { useRouter } from 'vue-router';

const router = useRouter()
const session = useSessionStore()

async function loginOrRegister(e) {
    if (!e) return
    e.preventDefault()
    console.log(e.target)

    let formData = new FormData(e.target)
    try {
        let req = await fetch(e.submitter.formAction, {
            method:e.target.method,
            body:formData,
        })
        if (!req.ok)
            throw new Error()
        let res = await req.json()
        localStorage.setItem("ACCESS_TOKEN", res.access)
        localStorage.setItem("REFRESH_TOKEN", res.refresh)
        session.isAuthenticated = true
        router.push("/")
    } catch (error) {
        console.log(error)
    }
}

</script>

<template>
    <div class="container m-auto flex flex-col items-center justify-center gap-4">
        <form @submit="(e) => {loginOrRegister(e)}" method="post" class="w-96 rounded-2xl p-4 bg-gray-100/75 backdrop-blur-sm flex flex-col gap-4 items-center">
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
                <button :formaction="`${localRoute}api/auth/register`" type="submit" class="basic_button text-base flex-1">Регистрация</button>
                <button :formaction="`${localRoute}api/auth/token`" type="submit" class="basic_button text-base flex-1">Вход</button>
            </div>
        </form>
    </div>
</template>