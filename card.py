class Card: # inherits from 'object'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # properties??
    def __str__(self):
        return f"Card:{self.rank}/{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("8", "Diamonds")
    print(c1.rank)
    print(c1.suit)
    print(c1)
