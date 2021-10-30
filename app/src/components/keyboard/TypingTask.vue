<template>
  <div class="typing-task">
    <span
      class="letter"
      v-for="l in visibleTaskPart"
      :key="l.i"
      :class="{
        highlighted: position === l.i,
        subHighlighted: Math.abs(position - l.i) < 5,
      }"
    >{{ l.letter }}</span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  props: [
    'task',
    'position',
  ],
  computed: {
    visibleTaskPart () {
      const targetFrom = this.position - 10
      const from = Math.max(0, targetFrom)
      const targetUntil = this.position + 10
      const until = Math.min(targetUntil, this.task.length)
      const letters = this.task.split('').slice(from, until).map((letter, i) => ({
        letter,
        i: from + i
      }))
      return this._antitrim(letters, from - targetFrom, 0)
    }
  },
  methods: {
    _antitrim (letters, before, after) {
      return this._makeArrayOfSpaces(before).concat(letters).concat(this._makeArrayOfSpaces(after))
    },
    _makeArrayOfSpaces (n) {
      const result = []
      for (let i = 0; i < n; i ++) {
        result.push({
          letter: '_',
          i: -Infinity
        })
      }
      return result
    }
  }
})
</script>

<style lang="stylus" scoped>
.typing-task
  text-align center
  font-size 3em
  .letter
    &.subHighlighted
      background-color yellow
    &.highlighted
      background-color orange
</style>
