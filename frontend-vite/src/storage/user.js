import {defineStore} from "pinia"
import { localRoute } from "../helper/constants"

export const useUserStore = defineStore('user', {
    state:() =>{
        return {
            id:undefined,
            username:"",
            profile:{
                fio:"",
                number:"",
                email:"",
                geo:"",
            },
            comments:[]
        }
    },

    actions:{
        async getMe(){
            let access = localStorage.getItem("ACCESS_TOKEN")
            try {
                let req = await fetch(`${localRoute}api/users`,{
                    headers:{
                        "Authorization":`Bearer ${access}`
                    }
                })
                if (!req.ok) 
                    return
                let res = await req.json()

                this.$patch(res.result)
/* 
                this.id = res.response.id
                this.username = res.response.username
                if (!res.profile) 
                    return
                this.profile.fio = res.response.profile.fio
                this.profile.number = res.response.profile.number
                this.profile.email = res.response.profile.email
                this.profile.geo = res.response.profile.geo */
                return res.result
            } catch (error) {
                console.error(error)
            }
        },
        async getComments(userID){
            let access = localStorage.getItem("ACCESS_TOKEN")
            let urlParams = new URLSearchParams({"user_id":userID})
            try {
                let req = await fetch(`${localRoute}api/comments?${urlParams}`,{
                    headers:{
                        "Authorization":`Bearer ${access}`
                    }
                })
                if (!req.ok) return
                let res = await req.json()
                this.comments = res.results
            } catch (error) {
                console.error(error)
            }
        },
        async updateData(newData) {
            let access = localStorage.getItem("ACCESS_TOKEN")
            try {
                let req = await fetch(`${localRoute}api/users`,{
                    method:"PATCH",
                    headers:{
                        "Authorization":`Bearer ${access}`,
                        "content-type":"application/json"
                    },
                    body:JSON.stringify(newData)
                })
                if (!req.ok) return
                let res = await req.json()
                this.$patch(res.result)
            } catch (error) {
                console.error(error)
            }            
        }
    }
})