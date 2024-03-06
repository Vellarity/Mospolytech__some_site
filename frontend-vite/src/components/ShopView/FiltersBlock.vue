<script setup>
import RoundedChecker from '../atoms/RoundedChecker.vue';
import { localRoute } from '../../helper/constants';
import {useFiltersStore} from "../../storage/filters"
import {useShopItemsStore} from "../../storage/shopItems"


const filtersStore = useFiltersStore()

const shopItemsStore = useShopItemsStore()

filtersStore.getTypes()
filtersStore.getMinMaxCost()

</script>

<template>
    <!-- 
    <div class="flex flex-col gap-1">
        <h3 class="font-semibold text-lg">
           Поиск 
        </h3>
        <input 
            class="flex-1 h-10 w-full p-1 rounded-xl border-2 border-gray-300 focus-visible:outline-gray-500 delay-150" 
            placeholder="Название продукта или производителя"
        >
    </div>
 -->
    <div class="flex flex-col gap-1">
        <h3 class="font-semibold text-lg">
            Категория 
        </h3>
        <ul>
            <template v-for="wearType in filtersStore.types">
                <li class="flex items-center gap-1">
                    <input @click="filtersStore.updateQueryType($event)" type="checkbox" class="h-4 w-4" :value="wearType.id"> <label class="text-base font-normal">{{wearType.name}}</label>
                </li>
            </template>

<!-- 
            <li class="flex items-center gap-1">
                <input type="checkbox" class="h-4 w-4"> <label class="text-base font-normal">Кофты</label>
            </li>
            <li class="flex items-center gap-1">
                <input type="checkbox" class="h-4 w-4"> <label class="text-base font-normal">Штаны</label>
            </li>
            <li class="flex items-center gap-1">
                <input type="checkbox" class="h-4 w-4"> <label class="text-base font-normal">Обувь</label>
            </li>  -->
        </ul>
    </div>

    <div class="flex flex-col gap-1">
        <h3 class="font-semibold text-lg">
            Цвет 
        </h3>

        <div class="flex gap-1">
            <RoundedChecker value="BLACK" selected-color-bg="bg-black" class-names="h-8 w-8"/>
            <RoundedChecker value="WHITE" selected-color-bg="bg-white" class-names="h-8 w-8"/>
            <RoundedChecker value="RED" selected-color-bg="bg-red-600" class-names="h-8 w-8"/>
            <RoundedChecker value="BLUE" selected-color-bg="bg-blue-600" class-names="h-8 w-8"/>
            <RoundedChecker value="GREEN" selected-color-bg="bg-green-600" class-names="h-8 w-8"/>
            <RoundedChecker value="PURPLE" selected-color-bg="bg-purple-600" class-names="h-8 w-8"/>
            <RoundedChecker value="YELLOW" selected-color-bg="bg-yellow-300" class-names="h-8 w-8"/>
        </div>
    </div>

    <div class="flex flex-col gap-1">
        <h3 class="font-semibold text-lg">
            Цена 
        </h3>

        <div class="flex gap-1">
            <input 
                @change="filtersStore.updateMinCost($event.target.value)"
                type="number"
                class="flex-1 h-10 w-1/2 p-1 rounded-lg border-2 border-gray-300 focus-visible:outline-gray-500 delay-150" 
                :min="filtersStore.minCost" 
                :max="filtersStore.maxCost"
                :placeholder="filtersStore.minCost"
            > 
            <input 
                @change="filtersStore.updateMaxCost($event.target.value)"
                type="number"
                class="flex-1 h-10 w-1/2 p-1 rounded-lg border-2 border-gray-300 focus-visible:outline-gray-500 delay-150" 
                :min="filtersStore.minCost" 
                :max="filtersStore.maxCost"
                :placeholder="filtersStore.maxCost"
            > <!-- TODO: MAX VALUE FROM SERVER -->
        </div>
    </div>

    <button @click="shopItemsStore.getList(filtersStore.activeFilters)" class="bg-gray-300 p-2 rounded-lg">
        Применить фильтры
    </button>


</template>