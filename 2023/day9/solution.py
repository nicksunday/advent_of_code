#!/usr/bin/env python3


def parse_input(file_name: str = 'input.txt') -> list:
    output = []
    with open(file_name, 'r', encoding='utf-8') as histories:
        for history in histories.readlines():
            output.append([int(i) for i in history.split()])
    return output


def part1():
    histories = parse_input() #'example.txt')
    totals = []
    for history in histories:
        sequences = [history]
        current_sequence = history
        while not all(i == 0 for i in current_sequence):
            current_sequence = [
                current_sequence[i + 1] - current_sequence[i]
                for i in range(len(current_sequence) - 1)
            ]
            sequences.append(current_sequence)
        totals.append(sum([i[-1] for i in sequences]))
    return sum(totals)


def part2():
    histories = parse_input() #'example.txt')
    totals = []
    for history in histories:
        sequences = [history]
        current_sequence = history
        while not all(i == 0 for i in current_sequence):
            current_sequence = [
                current_sequence[i + 1] - current_sequence[i]
                for i in range(len(current_sequence) - 1)
            ]
            sequences.append(current_sequence)
        #totals.append(sum([i[0] for i in sequences]))
        total = 0
        sequences.reverse()
        for i, sequence in enumerate(sequences):
            if i < len(sequences) - 1:
                sequences[i + 1].insert(0, sequences[i + 1][0] - sequence[0])
        totals.append(sequences[-1][0])
    return sum(totals)


if __name__ == '__main__':
    print(f"Part 1 total: {part1()}")
    print(f"Part 2 total: {part2()}")