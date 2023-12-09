#!/usr/bin/env python

from collections import Counter

class Card():
    label: str
    value: int

    def __init__(self, label: str, wilds: bool = False):
        self.label = label

        value_map = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10
        }
        if label.isnumeric():
            self.value = int(label)
        else:
            if wilds and label == 'J':
                self.value = 1
            else:
                self.value = value_map[label]
    
    def __eq__(self, other_card) -> bool:
        return self.value == other_card.value

    def __ne__(self, other_card) -> bool:
        return self.value != other_card.value

    def __lt__(self, other_card) -> bool:
        return self.value < other_card.value

    def __le__(self, other_card) -> bool:
        return self.value <= other_card.value

    def __gt__(self, other_card) -> bool:
        return self.value > other_card.value

    def __ge__(self, other_card) -> bool:
        return self.value >= other_card.value
    
    def __str__(self) -> str:
        return self.label


class Deck():
    cards: dict = {
        card: Card(card)
        for card in [
            'A', 'K', 'Q', 'J', 'T', '9', '8',
            '7', '6', '5', '4', '3', '2'
        ]
    }
    cards_with_jokers: dict = {
        card: Card(card, wilds = True)
        for card in [
            'A', 'K', 'Q', 'J', 'T', '9', '8',
            '7', '6', '5', '4', '3', '2'
        ]
    }


class Hand():
    hand_type: str
    cards: list
    card_frequency: Counter
    bet: int
    value: int
    rank: int
    deck: dict

    def __init__(self, hand: list, bet: int, deck: dict) -> None:
        self.cards = [deck[card] for card in hand]
        self.card_frequency = Counter(hand)
        self.bet = bet
        self.deck = deck
        self.determine_hand_type()

    def __eq__(self, other) -> bool:
        return all(
            self.cards[i] == other.cards[i]
            for i in range(len(self.cards))
        )

    def __ne__(self, other) -> bool:
        return not all(
            self.cards[i] == other.cards[i]
            for i in range(len(self.cards))
        )
    
    def __lt__(self, other) -> bool:
        if self.hand_type == other.hand_type:
            for i in range(len(self.cards)):
                if self.cards[i] != other.cards[i]:
                    return self.cards[i] < other.cards[i]
        else:
            return self.value < other.value

    def __gt__(self, other) -> bool:
        if self.hand_type == other.hand_type:
            for i in range(len(self.cards)):
                if self.cards[i] != other.cards[i]:
                    return self.cards[i] > other.cards[i]
        else:
            return self.value > other.value

    def __repr__(self) -> str:
        return f"{''.join([c.label for c in self.cards])}"

    def determine_hand_type(self) -> None:
        if len(self.card_frequency) == 1:
            self.hand_type = "Five of a kind"
            self.value = 7
        elif len(self.card_frequency) == 2:
            if any(value == 4 for value in self.card_frequency.values()):
                self.hand_type = "Four of a kind"
                self.value = 6
            else:
                self.hand_type = "Full house"
                self.value = 5
        elif len(self.card_frequency) == 3:
            if any(value == 3 for value in self.card_frequency.values()):
                self.hand_type = "Three of a kind"
                self.value = 4
            else:
                self.hand_type = "Two pair"
                self.value = 3
        elif len(self.card_frequency) == 4:
            self.hand_type = "One pair"
            self.value = 2
        else:
            self.hand_type = "High card"
            self.value = 1

    def set_rank(self, rank: int) -> None:
        self.rank = rank

    def increase_power(self) -> None:
        high_cards = []
        non_wilds = [c.label for c in self.cards if c.label != 'J']
        non_wilds_frequency = Counter(non_wilds)
        high_frequency = max([value for value in non_wilds_frequency.values()], default=0)
        for card in non_wilds:
            if self.card_frequency[card] == high_frequency:
                high_cards.append(card)
        joker_count = len(self.cards) - len(non_wilds)
        if len(set(high_cards)) == 2 and joker_count == 1:
            self.hand_type = "Full house"
            self.value = 5
        elif joker_count >= 1:
            if high_frequency + joker_count == 5:
                self.hand_type = "Five of a kind"
                self.value = 7
            elif high_frequency + joker_count == 4:
                self.hand_type = "Four of a kind"
                self.value = 6
            elif high_frequency + joker_count == 3:
                self.hand_type = "Three of a kind"
                self.value = 4
            elif high_frequency + joker_count == 2:
                self.hand_type = "One pair"
                self.value = 2
            