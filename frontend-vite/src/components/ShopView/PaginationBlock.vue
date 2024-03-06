<script setup>
import PaginationButton from '../atoms/PaginationButton.vue';

import {useShopItemsStore} from '../../storage/shopItems'

const shopItemsStore = useShopItemsStore()

import {useFiltersStore} from "../../storage/filters"

const filtersStore = useFiltersStore()

</script>

<template>
    <div class="flex w-100 gap-4 justify-between">

        <PaginationButton 
            v-if="shopItemsStore.pagination.prevPageLink" 
            @click="filtersStore.updatePage(shopItemsStore.pagination.thisPage-1); shopItemsStore.getList(filtersStore.activeFilters)"
            value="<" 
            />

        <!-- <div class="flex gap-1 justify-center flex-1">
            <PaginationButton @click="console.log(1)" :is-active="shopItemsStore.navigation.thisPage == 1" :value="'1'" />

            <div class="self-end" v-if="shopItemsStore.navigation.maxPages>1" >...</div>

            <template v-for="i in shopItemsStore.navigation.maxPages">
                <PaginationButton 
                    v-if="(i !== shopItemsStore.navigation.maxPages) && (i !== 1)" 
                    @click="console.log(1)" :is-active="shopItemsStore.navigation.thisPage == i" 
                    :value="i.toString()" 
                />
            </template>

            <div class="self-end" v-if="shopItemsStore.navigation.maxPages>1" >...</div>

            <PaginationButton @click="console.log(1)" :is-active="shopItemsStore.navigation.thisPage == shopItemsStore.navigation.maxPages" :value="shopItemsStore.navigation.maxPages" />
        
        </div> -->

        <div class="flex gap-1 justify-center flex-1">
            <template v-for="iter in shopItemsStore.pagination.iterPages">
                <PaginationButton  
                    v-if="iter" 
                    @click="filtersStore.updatePage(iter); shopItemsStore.getList(filtersStore.activeFilters)" 
                    :is-active="shopItemsStore.pagination.thisPage == iter" 
                    :value="iter.toString()" 
                />
                <div class="self-end" v-else >...</div>
            </template>
        </div>

        <PaginationButton 
            v-if="shopItemsStore.pagination.nextPageLink && shopItemsStore.pagination.maxPages !== 1" 
            @click="filtersStore.updatePage(shopItemsStore.pagination.thisPage+1); shopItemsStore.getList(filtersStore.activeFilters)"
            value=">" 
        />
    </div> 
</template>