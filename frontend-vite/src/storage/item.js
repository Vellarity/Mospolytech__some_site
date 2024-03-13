import { defineStore } from "pinia";
import { localRoute } from "../helper/constants";


export const useItemStore = defineStore('item', {
    state: () => {
        return {
            info:{
                name:"",
                size:[],
                color:"",
                cost:0,
                type:"",
                image:"",
                infoText:"",
            },
            comments:[]
        }
    },
    actions: {
        async getItem(itemID) {
            try {
                let req = await fetch(`${localRoute}api/wears/${itemID}`)
                let res = await req.json()
                this.info.name = res.name
                this.info.size = res.size
                this.info.color = res.color
                this.info.cost = res.cost
                this.info.type = res.type
                this.info.image = res.image_url
                this.info.infoText = res.info_text
            } catch (error) {
                console.error(error)
            }
        },
        async getComments(itemID) {
            try {
                let urlParams = new URLSearchParams({"wear_id":itemID})
                let req = await fetch(`${localRoute}api/comments?${urlParams}`)
                let res = await req.json()
                this.comments = res.results
            } catch (error) {
                console.error(error)
            }
        } 
    }
})