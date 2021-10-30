<template>
    <TypingTask :task="typingTask" :position="typingTaskPosition"/>
    <KeyboardLayout :map="kedmanee" :highlightedKey="typingTask[typingTaskPosition]" @keyPressed="onKeyPressed" ref="keyboardLayout"/>
    <LetterDetails :letter="typingTask[typingTaskPosition]"/>
</template>

<script language="ts">
import wlf from '../../../data/characters.json'
import { defineComponent } from 'vue'
import KeyboardLayout from '../components/keyboard/KeyboardLayout.vue'
import TypingTask from '../components/keyboard/TypingTask.vue'
import LetterDetails from '../components/keyboard/LetterDetails.vue'

export default defineComponent({
    components: {
        KeyboardLayout,
        TypingTask,
        LetterDetails,
    },
    data () {
        return {
            typingTaskPosition: 0
        }
    },
    computed: {
        typingTask () {
            return this._createRandomTask(100)
        },
        letters () {
            return wlf //.filter(l => l.frequency >= 0.03)
        },
        // taskLetters () {
        //     // return "านรอกเ"
        //     return "านรอกเง่มั"
        // },
        enabledLetters () {
            // return this.letters.filter(l => this.taskLetters.includes(l.letter))
            return this.letters.filter(l => l.type === "sonorant")
        },
        kedmanee () {
            return this.enabledLetters.reduce(
                (acc, l) => {
                    acc[l.keyboard_locations.kedmanee] = l.letter
                    return acc
                },
                {}
            )
        },
        frequencies () {
            return this.enabledLetters.reduce(
                (acc, l) => {
                    acc[l.letter] = l.frequency
                    return acc
                },
                {}
            )
        }
    },
    methods: {
        onKeyPressed (key) {
            const correct = this.typingTask[this.typingTaskPosition] === key
            // console.log(this.letters.find(l => l.letter === key), correct)
            if (correct) {
                this.typingTaskPosition++
                while (this.typingTask[this.typingTaskPosition] === ' ' ||
                    this.typingTask[this.typingTaskPosition] === '\n'
                ) {
                    this.typingTaskPosition++
                }
                if (this.typingTaskPosition >= this.typingTask.length) {
                    this.typingTaskPosition = 0
                }
            }
            setTimeout(() => this.$refs.keyboardLayout.resetPressedKey(), 0)
        },
        _createRandomTask (n) {
            const result = []
            for (let i = 0; i < n; i++) {
                result.push(this._getRandomEnabledLetter())
            }
            return result.join('')
        },
        _getRandomEnabledLetter (n) {
            const el = this.enabledLetters
            const i = Math.floor(Math.random() * el.length)
            return el[i].letter
        }
    }
})
</script>

<style lang="stylus" scoped>
.letter-details
  position absolute
  right 1em
  top 1em
</style>
