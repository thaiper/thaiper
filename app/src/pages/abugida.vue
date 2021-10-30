<template>
  <div class="page page-character-list">
    <CharacterList :characters="characters"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CharacterList from '../components/characters/CharacterList.vue'
import abugida from '../../../data/abugidaDetails.json'

export default defineComponent({
  components: {
    CharacterList,
  },
  computed: {
    characters () {
      const result = {}
      for (let k in abugida) {
        const c = abugida[k]
        if (c.character) {
          result[k] = { ...c }
        }
      }
      return result
    }
  }
})
</script>

<style lang="stylus">
.home-page
  //
</style>
