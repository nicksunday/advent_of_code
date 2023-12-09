#!/usr/bin/env python3


def parse_input(file_name: str = 'input.txt') -> dict:
    scratcher_dict = {}
    with open(file_name, 'r', encoding='utf-8') as scratchers:
        for line in scratchers.readlines():
            card_name, data = line.strip().split(':')
            card = int(card_name.split()[-1])
            winning_str, actual_str = data.split('|')
            winning = winning_str.strip().split()
            actual = actual_str.strip().split()
            scratcher_dict[card] = {
                "winning": winning,
                "actual": actual,
                "matches": 0,
                "copies": 1
            }
    return scratcher_dict


def part1() -> int:
    scratchers = parse_input() #'example.txt')
    grand_total = 0
    for card in scratchers:
        card_total = 0
        for number in scratchers.get(card).get("winning"):
            if number in scratchers.get(card).get("actual"):
                if card_total > 0:
                    card_total *= 2
                else:
                    card_total = 1
        # print(f"{card}: {card_total} points")
        grand_total += card_total
    return grand_total


def part2() -> int:
    scratchers = parse_input() # 'example.txt')
    grand_total = 0
    for card in scratchers:
        for number in scratchers.get(card).get("winning"):
            if number in scratchers.get(card).get("actual"):
                scratchers[card]['matches'] += 1
        for _ in range(scratchers.get(card).get("copies")):
            for i in range(scratchers.get(card).get("matches")):
                next_card = scratchers.get(card + 1 + i, None)
                if next_card:
                    scratchers[card + 1 + i]['copies'] += 1
    for card in scratchers:
        # print(scratchers.get(card))
        grand_total += scratchers.get(card).get("copies")
    return grand_total


if __name__ == '__main__':
    print(f"Part 1 Total: {part1()}")
    print(f"Part 2 Total: {part2()}")