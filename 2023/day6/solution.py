#!/usr/bin/env python3

import math

def parse_input(file_name: str = 'input.txt') -> list:
    with open(file_name, 'r', encoding='utf-8') as races_data:
        races = races_data.read()
        times, distances = races.split('\n')
        return [
            data_pair
            for data_pair in
            zip(
                map(int, times.split(':')[-1].split()),
                map(int, distances.split(':')[-1].split())
            )
        ]


def get_winning_solutions(time_allowed: int, distance: int) -> int:
    winners = 0
    button_range = range(0, time_allowed)
    time_range = range(time_allowed, 0, -1)
    for i in button_range:
        if button_range[i] * time_range[i] > distance:
            winners += 1
    return winners


def part1() -> int:
    data = parse_input() # 'example.txt')
    winner_count = []
    for time, distance in data:
        winner_count.append(get_winning_solutions(time, distance))
    return math.prod(winner_count)
    

def part2() -> int:
    data = parse_input() #'example.txt')
    time = ""
    distance = ""
    for t, d in data:
        time += f"{str(t)}"
        distance += f"{str(d)}"
    # print(time)
    # print(distance)
    return get_winning_solutions(int(time), int(distance))



if __name__ == '__main__':
    print(f"Part 1 Total: {part1()}")
    print(f"Part 2 Total: {part2()}")