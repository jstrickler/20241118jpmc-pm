import random
from playingcard import PlayingCard

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __repr__(self):
        my_type = type(self)
        return f"{my_type.__name__}()"

    def __len__(self):
        return len(self._cards)
    
    def __str__(self):
        my_type = type(self)
        return f"{my_type.__name__}({len(self)})"

if __name__ == "__main__":
    cd1 = CardDeck()
    cd2 = CardDeck()
    cd1.shuffle()
    # 
    print(f"{cd1 = }")
    print(f"{cd2 = }")
    print(cd1.cards)
    print()
    for i in range(5):
        card = cd1.draw()
        print(card)
    print(f"{len(cd1) = }")
    print(cd1)