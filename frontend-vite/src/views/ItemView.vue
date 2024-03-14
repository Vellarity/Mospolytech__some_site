<script setup>
import { useItemStore } from '../storage/item';
import { useRoute } from 'vue-router'
import InfoBlock from '../components/ItemView/InfoBlock.vue';
import CommentsBlock from '../components/ItemView/CommentsBlock.vue';

const route = useRoute()
const itemID = route.params.itemID

const itemStore = useItemStore()

itemStore.getItem(itemID)
itemStore.getComments(itemID)
</script>

<template>
    <div class="container mx-auto flex flex-col gap-4 mb-4">
        <InfoBlock :info="itemStore.info"/>
        <CommentsBlock :comments="itemStore.comments"/>
    </div>
</template>