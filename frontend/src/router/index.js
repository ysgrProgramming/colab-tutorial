import { createRouter, createWebHistory } from 'vue-router'
import DeckListView from '../views/DeckListView.vue'
import CardEditView from '../views/CardEditView.vue'
import StudyView from '../views/StudyView.vue'

import DeckCreateView from '../views/DeckCreateView.vue'

const routes = [
    { path: '/', component: DeckListView },
    { path: '/decks', component: DeckListView },
    { path: '/decks/create', component: DeckCreateView },
    { path: '/decks/:id', component: CardEditView },
    { path: '/study/:id', component: StudyView },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
