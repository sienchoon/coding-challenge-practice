# Blackjack using OOP

import random

class Player():
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0
        self.aces = 0
        
    def add_card(self, card):
        self.hand.append(card)
        self.points += card


class Deck():
    
    def __init__(self):
        self.suits = ['♠️', '♦️', '♣️', '♥️']
        self.numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        
        for suit in self.suits:
            for number in self.numbers:
                self.cards.append((number, suit))

# Create an instance of the Deck class
my_deck = Deck()

# Access attributes
print("Suits:", my_deck.suits)
print("Numbers:", my_deck.numbers)

# Access cards
print("Number of cards in the deck:", len(my_deck.cards))

# Example: Print the first 5 cards in the deck
print("First 5 cards in the deck:")
for card in my_deck.cards[:5]:
    print(card)
    