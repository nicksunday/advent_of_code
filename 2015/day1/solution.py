#!/usr/bin/env python3
from collections import Counter

def part1():
    with open('input.txt', 'r') as fin:
        floors = Counter(fin.read())
    print(floors["("] - floors[")"])
        
def part2():
    position = 0
    location = 0
    with open('input.txt', 'r') as fin:
        for floor in fin.read():
            position += 1
            if floor == "(":
                location += 1
            elif floor == ")":
                location -= 1
            if location == -1:
                break
    print(position)

if __name__ == "__main__":
    part1()
    part2()