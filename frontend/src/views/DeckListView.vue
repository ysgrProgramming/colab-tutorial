<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800">My Decks</h1>
      <router-link
        to="/decks/create"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        + Create Deck
      </router-link>
    </div>

    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-500">Loading decks...</p>
    </div>

    <div v-else-if="decks.length === 0" class="text-center py-12 bg-white rounded shadow">
      <p class="text-gray-500 mb-4">No decks found.</p>
      <router-link
        to="/decks/create"
        class="text-blue-600 hover:underline"
      >
        Create your first deck
      </router-link>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="deck in decks"
        :key="deck.id"
        class="bg-white p-6 rounded-lg shadow hover:shadow-md transition border border-gray-200"
      >
        <h2 class="text-xl font-semibold mb-2 text-gray-800">{{ deck.title }}</h2>
        <p class="text-sm text-gray-500 mb-4">Created: {{ new Date(deck.created_at).toLocaleDateString() }}</p>
        <div class="flex justify-between items-center">
          <router-link
            :to="`/decks/${deck.id}`"
            class="text-blue-600 hover:text-blue-800 font-medium"
          >
            Edit Cards
          </router-link>
          <router-link
            :to="`/study/${deck.id}`"
            class="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 text-sm"
          >
            Study
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getDecks } from '../api/decks'

const decks = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    decks.value = await getDecks()
  } catch (error) {
    console.error('Failed to fetch decks', error)
  } finally {
    loading.value = false
  }
})
</script>
