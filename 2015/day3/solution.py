#!/usr/bin/env python3

def parse_input(input_file = "input.txt"):
    with open(input_file, 'r') as fin:
        return fin.read().strip()

def part1():
    coordinate = (0, 0)
    visited = set([coordinate])
    for direction in parse_input():
        match direction:
            case "^":
                # Going up Y-axis
                x, y = coordinate
                coordinate = (x, y + 1)
            case "v":
                # Going down Y-axis
                x, y = coordinate
                coordinate = (x, y - 1)
            case ">":
                # Going right on X-axis
                x, y = coordinate
                coordinate = (x + 1, y)
            case "<":
                # Going left on X-axis
                x, y = coordinate
                coordinate = (x - 1, y)
        visited.add(coordinate)
    print(f"Part 1: {len(visited)}")

def part2():
    santa = (0, 0)
    robosanta = (0, 0)
    swap = False
    visited = set([santa, robosanta])
    for direction in parse_input():
        if swap:
            coordinate = robosanta
        else:
            coordinate = santa
        match direction:
            case "^":
                # Going up Y-axis
                x, y = coordinate
                coordinate = (x, y + 1)
            case "v":
                # Going down Y-axis
                x, y = coordinate
                coordinate = (x, y - 1)
            case ">":
                # Going right on X-axis
                x, y = coordinate
                coordinate = (x + 1, y)
            case "<":
                # Going left on X-axis
                x, y = coordinate
                coordinate = (x - 1, y)
        visited.add(coordinate)
        if swap:
            robosanta = coordinate
            swap = False
        else:
            santa = coordinate
            swap = True
    print(f"Part 2: {len(visited)}")

if __name__ == "__main__":
    part1()
    part2()