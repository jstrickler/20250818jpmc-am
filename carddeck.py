import random
from card import Card

class Game:
    def play(self):
        print("PLAYING")

class CardDeck(Game):
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()
    
    def __init__(self):
        self._cards = None
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:  # CardDeck.SUITS
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):  # getter property
        return self._cards

    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(d1)
    print(d1._cards)  # naughty!
    print(d1.cards)   # nice1
    d1.shuffle()
    for i in range(5):
        card = d1.draw()
        print(card)
    d1.play()