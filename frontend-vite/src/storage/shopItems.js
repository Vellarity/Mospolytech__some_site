import {defineStore} from "pinia"
import { localRoute } from "../helper/constants"

export const useShopItemsStore = defineStore('shopItems', {
    state: () => {
        return {
            itemsList:[],
            pagination:{
                maxPages: undefined,
                thisPage: 1,
                nextPageLink:null,
                prevPageLink:null,
                iterPages:[],
            }
        }
    },
    actions: {
        async getList(searchParams={}) {
            try {
                let urlParams = new URLSearchParams()
                for (const [name, param] of Object.entries(searchParams)) {
                    if(Array.isArray(param)) param.forEach(item => urlParams.append(`${name}`, item))
                    else urlParams.append(name, param)
                }
                console.log(urlParams.toString())
                let req = await fetch(`${localRoute}api/wears/shop_list?${urlParams}`)
                let res = await req.json()
                this.itemsList = res.results
                this.pagination.nextPageLink = res.links.next
                this.pagination.prevPageLink = res.links.previous
                this.pagination.thisPage = res.this_page
                this.pagination.maxPages = res.last_page
                this.pagination.iterPages = res.iter_pages
            } catch (error) {
                console.log(error)
                this.itemsList = []
            }
        },
        async searchList(searchParams, urlParams=null) {
            try {
                let params = new URLSearchParams(urlParams)
                let req = await fetch(`${localRoute}api/shop_list?${URLSearchParams}`, {
                    method:"POST",
                    body: JSON.stringify(searchParams),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                let res = await req.json()
                this.itemsList = res.results
                this.pagination.nextPageLink = res.links.next
                this.pagination.prevPageLink = res.links.previous
                this.pagination.thisPage = res.this_page
                this.pagination.maxPages = res.last_page
                this.pagination.iterPages = res.iter_pages
            } catch (error) {
                this.itemsList = []
            }
        }
    }
})