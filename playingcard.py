class PlayingCard:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self): # getter property
        return self._rank

    @property
    def suit(self):
        return self._suit
    # suit = property(suit)

    def __str__(self):  # str(obj)  len(), + / * % ** []
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"PlayingCard('{self.rank}', '{self.suit}')"
    
    def as_dict(self):
        return {'rank': self.rank, 'suit': self.suit}

if __name__ == "__main__":  # if this script run directly NOT imported as a module
    pc = PlayingCard("8", "Diamonds")
    print(f"{pc = }")  # repr()
    print(pc)   # str()
    # r = pc.get_rank()
    r = pc.rank
    print(f"{r = }")
    print(f"{type(PlayingCard.suit) = }")
    print(f"{pc.suit = }")
    print(f"{pc.as_dict() = }")
    print(f"{pc.__dict__ = }")
    
    
    
