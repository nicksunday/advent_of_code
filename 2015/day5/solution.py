#!/usr/bin/env python3

import re

def parse_input(filename: str = 'input.txt') -> list:
    naughty_list = []
    with open(filename, 'r') as fin:
        for item in fin.readlines():
            naughty_list.append(item.strip())
    return naughty_list

def part1():
    naughty_list = parse_input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    disallowed = ['ab', 'cd', 'pq', 'xy']
    nice = []
    for item in naughty_list:
        vowel_count = 0
        duplicate = False
        current = None
        last = None
        if any(d in item for d in disallowed):
            continue
        for c in item:
            last = current
            current = c
            if last == current:
                duplicate = True
            if c in vowels:
                vowel_count += 1
        if vowel_count >= 3 and duplicate:
            # print(f"{item} - {vowel_count} - {duplicate}")
            nice.append(item)
    print(f"Part 1: {len(nice)}")

def part2():
    naughty_list = parse_input()
    nice = []
    for item in naughty_list:
        has_pair = re.search(r'(..).*\1', item)
        has_repeat = re.search(r'(.).\1', item)
        if has_pair and has_repeat:
            nice.append(item)
    print(f"Part 2: {len(nice)}")


if __name__ == "__main__":
    part1()
    part2()
