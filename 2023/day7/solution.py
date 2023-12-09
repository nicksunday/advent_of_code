#!/usr/bin/env python3

from camel_cards import Card, Deck, Hand


def parse_input(file_name: str = 'input.txt', deck: Deck = Deck.cards) -> dict:
    data = []
    with open(file_name, 'r', encoding='utf-8') as camel_cards:
        for line in camel_cards.readlines():
            cards, bid = line.strip().split()
            data.append(
                Hand([c for c in cards], int(bid), deck)
            )
    return data


def part1() -> int:
    data = parse_input() # 'test1.txt') #'example.txt')
    sorted_data = sorted(data)
    for i in range(len(sorted_data)):
        sorted_data[i].rank = i + 1
    # for hand in sorted_data:
    #    print(hand, hand.bet, hand.hand_type)
    winnings = [hand.bet * hand.rank for hand in sorted_data]
    return sum(winnings)


def part2() -> int:
    data = parse_input(deck = Deck.cards_with_jokers, file_name = 'input.txt') #'test1.txt') #'example.txt')
    for hand in data:
        #print(hand)
        #print(f"    Old type: {hand.hand_type}")
        hand.increase_power()
        #print(f"    New type: {hand.hand_type}")
    sorted_data = sorted(data)
    for i in range(len(sorted_data)):
        sorted_data[i].rank = i + 1
        #print(sorted_data[i], sorted_data[i].bet, sorted_data[i].hand_type)
    winnings = [hand.bet * hand.rank for hand in sorted_data]
    #for hand in sorted(data):
    #    print(hand, hand.bet)
    return sum(winnings)


if __name__ == '__main__':
    #part1()
    print(f"Part 1 Winnings: {part1()}")
    #part2()
    print(f"Part 2 Winnings: {part2()}")
