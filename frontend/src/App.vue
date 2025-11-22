<template>
  <div class="min-h-screen flex flex-col bg-gray-100">
    <header class="bg-blue-600 text-white p-4 shadow-md">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-xl font-bold">FlashLearn</h1>
        <nav>
          <router-link to="/" class="px-3 py-2 hover:bg-blue-700 rounded">Home</router-link>
          <router-link to="/decks" class="px-3 py-2 hover:bg-blue-700 rounded">Decks</router-link>
        </nav>
      </div>
    </header>

    <main class="flex-grow container mx-auto p-4">
      <router-view></router-view>
    </main>

    <footer class="bg-gray-800 text-white p-4 text-center">
      <p>&copy; 2024 FlashLearn</p>
    </footer>
  </div>
</template>
