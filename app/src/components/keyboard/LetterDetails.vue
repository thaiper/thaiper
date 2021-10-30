<template>
  <div class="letter-details" :class="{
    [dossier.type]: true,
    [dossier.class]: true,
  }">
    <h1>{{ letter }}</h1>
    <div class="trait name" v-if="dossier.name"><strong>{{ dossier.name }}</strong></div>
    <div class="trait transcriptions" v-if="dossier.transcriptions">
      transcriptions:
      <span class="latin" v-if="dossier.transcriptions.latin">{{ dossier.transcriptions.latin }}</span>
      <span class="cyrillic" v-if="dossier.transcriptions.cyrillic">{{ dossier.transcriptions.cyrillic }}</span>
    </div>
    <div class="trait class" v-if="dossier.class">class: <strong>{{ dossier.class }}</strong></div>
    <div class="trait type" v-if="dossier.type">type: <strong>{{ dossier.type }}</strong></div>
    <div class="trait frequency" v-if="dossier.frequency">frequency: <strong>{{ Math.round(dossier.frequency * 1000) / 10 }}%</strong></div>
    <audio ref="audio" v-if="abugidaPosition" :src="`/audio-samples/abugida/${abugidaPosition}.mp3`" autoplay/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import wlf from '../../../../data/characters.json'
import abugidaDetails from '../../../../data/abugidaDetails.json'

export default defineComponent({
  props: [
    'letter',
  ],
  computed: {
    dossier () {
      return wlf.find(l => l.letter === this.letter)
    },
    abugidaPosition () {
      const ap = abugidaDetails[this.letter].abugidaPosition
      return ap == 4
        ? 3
        : ap > 5
          ? ap - 2
          : ap
      }
  }
})
</script>

<style lang="stylus" scoped>
.letter-details
  &.low
    h1, .class
      background-color lightblue
  &.mid
    h1, .class
      background-color lightgreen
  &.high
    h1, .class
      background-color lightyellow
  &.vowel
    h1, .class
      background-color pink

  &.sonorant
    .type
      background-color lightblue
  &.unaspirated
    .type
      background-color rgba(0, 255, 0, 100)

  h1
    margin 0
    padding 0 .1em
    font-size 10em
    color black
    min-width 1em
    text-align center

  .trait
    padding .5em
    margin .5em 0

    &.name
      font-size 3em
      padding 0.1em
      margin 0
      text-align center

  .transcriptions
    > span
      display inline-block
      margin-right .5em
      font-weight bold
      font-size 1.5em

</style>
