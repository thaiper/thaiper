<template>
    <div class="character-list">
        <!-- <div v-for="(c, i) in characters" :key="i">{{ c }}</div> -->
        <Character v-for="c in characters" :character="c" :key="c.abugidaPosition"/>
    </div>
</template>

<script language="ts">
import { defineComponent } from 'vue'
import Character from './Character.vue'

export default defineComponent({
    components: {
        Character
    },
    props: [
        'characters'
    ],
})
</script>

<style lang="stylus" scoped>
.character-list
    //
</style>
