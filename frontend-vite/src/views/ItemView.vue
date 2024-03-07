<script setup>
import { useItemStore } from '../storage/item';
import { useRoute } from 'vue-router'
import InfoBlock from '../components/ItemView/InfoBlock.vue';

const route = useRoute()
const itemID = route.params.itemID

const itemStore = useItemStore()

itemStore.getItem(itemID)
itemStore.getComments(itemID)
</script>

<template>
    <div class="container">
        <InfoBlock :info="itemStore.info"/>
    </div>
</template>