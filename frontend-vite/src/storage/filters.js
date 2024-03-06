import {defineStore} from "pinia"

import { localRoute } from "../helper/constants"

export const useFiltersStore = defineStore('filters', {
    state: () => {
        return {
            types: [],
            maxCost:0,
            minCost:0,
            activeFilters:{
                types:[],
                colors:[],
                minCost:"0",
                maxCost:"0",
                searchParam:"",
                page:1,
            }
        }
    },
    actions: {
        async getTypes() {
            try {
                let req = await fetch(`${localRoute}api/filters/types`)
                let res = await req.json()
                if (res.error === false)
                    this.types = res.data
            } catch (error) {
                
            }
        },
        async getMinMaxCost() {
            try {
                let req = await fetch(`${localRoute}api/filters/costs`)
                let res = await req.json()
                if (res.error === false) {
                    this.minCost = res.data.min
                    this.maxCost = res.data.max
                }
            } catch (error) {
                
            }
        },
        updateQueryType(event) {
            if (event.target.checked)
                this.activeFilters.types.push(event.target.value)
            else 
                this.activeFilters.types = this.activeFilters.types.filter(item => item !== event.target.value)
        },
        updateQueryColor(isChecked, color) {
            if (isChecked)
                this.activeFilters.colors.push(color)
            else 
                this.activeFilters.colors = this.activeFilters.colors.filter(item => item !== color)
        },
        updateMinCost(value) {
            this.activeFilters.minCost = value || 0
        },
        updateMaxCost(value) {
            this.activeFilters.maxCost = value || 0
        },
        updateSearchParam(value) {
            this.activeFilters.searchParam = value
        },
        updatePage(pageNumber) {
            this.activeFilters.page = pageNumber
        }
    }
})