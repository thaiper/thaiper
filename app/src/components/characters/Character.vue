<template>
    <div class="character" :class="frequencyClass(character.frequency)">
      <span class="char">{{ character.character }}</span>
      <span class="class">{{ character.class }}</span>
      <span class="frequency">{{ frequency_to_string }}</span>
    </div>
</template>

<script language="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props: [
        'character'
    ],
    computed: {
        frequency_to_string () {
            return `${Math.floor(this.character.frequency * 10000) / 100 }%`
        }
    },
    methods: {
        frequencyClass (f) {
            return f > 0.04
                ? 'most-frequent'
                : f > 0.03
                    ? 'quite-frequent'
                    : f > 0.02
                    ? 'mid-frequent'
                    : f > 0.01
                        ? 'rarish'
                        : f > 0.001
                        ? 'rare'
                        : 'ultra-rare'
        }
    }
})
</script>

<style lang="stylus" scoped>
.character
    display inline-block
    padding .2em
    margin .2em
    border 1px solid black
    font-size 2em
    .char
        display block
    .class
        display block
        text-align center
    &.most-frequent
        background-color lightgreen
        > .char
            font-size 6em
    &.quite-frequent
        background-color lightblue
        > .char
            font-size 5em
    &.mid-frequent
        background-color pink
        > .char
            font-size 4em
    &.rarish
        background-color orange
        > .char
            font-size 3em
    &.rare
        background-color lightyellow
        > .char
            font-size 2em
    &.ultra-rare
        background-color lightgray
        > .char
            font-size 1.5em
</style>
