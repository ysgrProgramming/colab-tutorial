// Mock data
let decks = [
    { id: 1, title: 'English Vocabulary', created_at: '2023-11-01T10:00:00Z' },
    { id: 2, title: 'Python Basics', created_at: '2023-11-02T11:00:00Z' },
]

export const getDecks = async () => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve([...decks])
        }, 500)
    })
}

export const createDeck = async (title) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            const newDeck = {
                id: decks.length + 1,
                title,
                created_at: new Date().toISOString(),
            }
            decks.push(newDeck)
            resolve(newDeck)
        }, 500)
    })
}

export const getDeck = async (id) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const deck = decks.find(d => d.id === Number(id))
            if (deck) {
                // Mock cards if not present
                if (!deck.cards) {
                    deck.cards = [
                        { id: 1, question: 'Apple', answer: 'りんご', explanation: 'A red fruit' },
                        { id: 2, question: 'Dog', answer: '犬', explanation: 'A loyal animal' },
                    ]
                }
                resolve(deck)
            } else {
                reject(new Error('Deck not found'))
            }
        }, 500)
    })
}

export const addCard = async (deckId, card) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const deck = decks.find(d => d.id === Number(deckId))
            if (deck) {
                const newCard = { ...card, id: Date.now() } // Simple ID generation
                if (!deck.cards) deck.cards = []
                deck.cards.push(newCard)
                resolve(newCard)
            } else {
                reject(new Error('Deck not found'))
            }
        }, 500)
    })
}

export const deleteCard = async (deckId, cardId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const deck = decks.find(d => d.id === Number(deckId))
            if (deck && deck.cards) {
                deck.cards = deck.cards.filter(c => c.id !== cardId)
                resolve()
            } else {
                reject(new Error('Deck or card not found'))
            }
        }, 500)
    })
}
