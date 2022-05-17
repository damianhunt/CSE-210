import random

class Card:

    ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    suits = ["Clubs","Hearts","Diamonds","Spades"]
    deck = []

    value = 1
    for rank in ranks:
        for suit in suits:
            deck.append([rank + " of " + suit, value])
        value = value + 1

    random.shuffle(deck)
    score = 0
    card1 = deck.pop(0)
