import { defineStore } from "pinia";
import { localRoute } from "../helper/constants";


export const useItemStore = defineStore('item', {
    state: () => {
        return {
            name:String,
            sizes:Array,
            color:String,
            cost:Number,
            type:String,
            comments:Array
        }
    },
    actions: {
        async getItem(itemID) {
            try {
                let req = await fetch(`${localRoute}/items/${itemID}`)
                let res = await req.json()
                this.name = res.data.name
                this.sizes = res.data.sizes
                this.color = res.data.color
                this.cost = res.data.cost
                this.type = res.data.type
                this.comments = res.data.comments
            } catch (error) {
                console.error(error)
            }
        }
    }
})