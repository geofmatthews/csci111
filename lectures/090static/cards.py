class Card:
    """Represents a standard playing card."""
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

    @classmethod
    def card(cls, suit= 'Spades', rank='Ace'):
        sindex = cls.suit_names.index(suit)
        rindex = cls.rank_names.index(rank)
        return cls(sindex, rindex)

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # suits are the same... check ranks
        return self.rank < other.rank

print(Card())
print(Card.card())
    
class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)
            
    def shuffle(self):
        random.shuffle(self.cards)

        
class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
