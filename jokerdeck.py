from playingcard import PlayingCard
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck() # call parent method
        joker1 = PlayingCard('**JOKER1**', '**JOKER1**')
        joker2 = PlayingCard('**JOKER2**', '**JOKER2**')
        self._cards.append(joker1)
        self._cards.append(joker2)

if __name__ == "__main__":
    j = JokerDeck()
    print(f"{j = }")
    j.shuffle()
    print(f"{j.cards = }")
