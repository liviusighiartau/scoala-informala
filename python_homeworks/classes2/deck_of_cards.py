import random


class Deck(object):
    def __init__(self, suits: list, values: list):
        self.deck_cards = []
        for suit_ in suits:
            for value_ in values:
                self.deck_cards.append(Card(suit_, value_))

    def deal_card(self):
        return self.deck_cards.pop()

    def shuffle_cards(self):
        if len(self.deck_cards) < 52:
            raise Exception("The deck of cards is incomplete!")
        else:
            random.shuffle(self.deck_cards)

    def print_deck(self):
        print(len(self.deck_cards))


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_card(self):
        message = f'{self.value} of {self.suit}'
        print(message)


card_1 = Card('Hearts', 'A')
# card_1.print_card()
card_2 = Card('Clubs', 'A')
# card_2.print_card()

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = Deck(suits, values)

deck.print_deck()
dealt_card = deck.deal_card()
dealt_card.print_card()
deck.print_deck()

deck.shuffle_cards()
