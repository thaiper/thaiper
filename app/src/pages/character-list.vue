<template>
  <div class="page page-character-list">
    <CharacterList :characters="characters"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CharacterList from '../components/characters/CharacterList.vue'

export default defineComponent({
  components: {
    CharacterList,
  },
  computed: {
    characters () {
      return [
        {
            "frequency": 0.063,
            "character": "า",
            "type": "long vowel",
            "class": "vowel",
            "transcriptions": {
                "latin": "a:",
                "cyrillic": "а:"
            },
            "keyboard_locations": {
                "kedmanee": "k"
            }
        },
        {
            "frequency": 0.0565,
            "character": "น",
            "name": "หนู",
            "type": "sonorant",
            "class": "low",
            "keyboard_locations": {
                "kedmanee": "o"
            },
            "transcriptions": {
                "latin": "n",
                "cyrillic": "н"
            }
        },
      ]
    }
  }
})
</script>

<style lang="stylus">
.home-page
  //
</style>
