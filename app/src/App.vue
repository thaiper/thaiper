<template>
  <PrimaryNavigation/>
  <router-view></router-view>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import PrimaryNavigation from './components/layout/PrimaryNavigation.vue'

export default defineComponent({
  name: 'App',
  components: {
    PrimaryNavigation,
  },
})
</script>

<style lang="stylus">
#app
  //
</style>
