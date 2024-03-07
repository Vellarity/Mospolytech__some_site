import { defineStore } from "pinia";
import { localRoute } from "../helper/constants";


export const useItemStore = defineStore('item', {
    state: () => {
        return {
            info:{
                name:String,
                sizes:Array,
                color:String,
                cost:Number,
                type:String,
            },
            comments:Array
        }
    },
    actions: {
        async getItem(itemID) {
            try {
                let req = await fetch(`${localRoute}api/wears/${itemID}`)
                let res = await req.json()
                this.info.name = res.name
                this.info.sizes = res.sizes
                this.info.color = res.color
                this.info.cost = res.cost
                this.info.type = res.type
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