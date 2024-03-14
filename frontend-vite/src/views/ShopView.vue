<script setup>
import { onMounted } from 'vue';
import FiltersBlock from '../components/ShopView/FiltersBlock.vue';
import ItemCard from "../components/ShopView/ItemCard.vue"
import PaginationBlock from '../components/ShopView/PaginationBlock.vue';
import {useShopItemsStore} from '../storage/shopItems'

const shopItemsStore = useShopItemsStore()

import {useFiltersStore} from "../storage/filters"

const filtersStore = useFiltersStore()

shopItemsStore.getList()

</script>

<template>
    <div class="container grid grid-cols-shopBlock gap-4 mx-auto mb-4">
        <aside class="bg-gray-100/75 backdrop-blur-sm rounded-2xl col-start-1 p-4 gap-4 h-min  flex flex-col">
            <h2 class="font-semibold text-xl">
                Фильтры:
            </h2>

            <FiltersBlock />
        </aside>
        <div class="flex flex-col gap-4">

            <div class="w-full flex border-2 border-gray-100 rounded-2xl">
                <input 
                    @change="filtersStore.updateSearchParam($event.target.value)"
                    type="text" 
                    placeholder="Название продукта"
                    class="w-full h-full rounded-l-xl py-3 px-2 focus-visible:outline-gray-500"
                >
                <button
                    @click="shopItemsStore.getList(filtersStore.activeFilters)"
                    class="bg-gray-100 w-28 rounded-r-xl flex justify-center items-center"
                >
                    <span class="icon icon-search icon-28" />
                </button>
            </div>

            <div class="grid grid-cols-3 2xl:grid-cols-4 gap-3">
                <template v-if="shopItemsStore.itemsList.length" v-for="item in shopItemsStore.itemsList">
                    <ItemCard :shop-item="item"/>
                </template>
                <template v-else>
                    <div>
                        Ничего не найдено. Попробуйте поменять фильтры.
                    </div>
                </template>
            </div>

            <PaginationBlock />

        </div>
    </div>
</template>