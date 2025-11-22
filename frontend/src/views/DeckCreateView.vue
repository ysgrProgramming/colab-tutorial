<template>
  <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-4">Create New Deck</h1>
    <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label for="title" class="block text-gray-700 font-bold mb-2">Title</label>
        <input
          v-model="title"
          type="text"
          id="title"
          class="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="e.g., English Vocabulary"
          required
        />
      </div>
      <div class="flex justify-end gap-2">
        <router-link to="/decks" class="px-4 py-2 text-gray-600 hover:text-gray-800">Cancel</router-link>
        <button
          type="submit"
          class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
          :disabled="isSubmitting"
        >
          {{ isSubmitting ? 'Creating...' : 'Create' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createDeck } from '../api/decks'

const router = useRouter()
const title = ref('')
const isSubmitting = ref(false)

const handleSubmit = async () => {
  if (!title.value) return
  
  isSubmitting.value = true
  try {
    await createDeck(title.value)
    router.push('/decks')
  } catch (error) {
    console.error('Failed to create deck', error)
    alert('Failed to create deck')
  } finally {
    isSubmitting.value = false
  }
}
</script>
