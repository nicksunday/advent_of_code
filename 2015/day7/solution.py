#!/usr/bin/env python3

import re

def parse_input(f: str = 'example.input.txt') -> list:
    with open(f, 'r', encoding='utf-8') as fin:
        instructions = [line.strip() for line in fin.readlines()]
    return instructions

def replace_bitwise(text: str) -> str:
    text = re.sub(r'\bNOT\s+([a-z0-9]+)\b', r'(~\1 & 0xFFFF)', text)
    text = re.sub(r'\b([a-z0-9]+)\s+LSHIFT\s+(\d+)\b', r'((\1 << \2) & 0xFFFF)', text)

    replacements = {
        'AND': '&',
        'OR': '|',
        'RSHIFT': '>>',
    }
    pattern = r'\b(?:' + '|'.join(map(re.escape, replacements.keys())) + r')\b'
    text = re.sub(pattern, lambda m: replacements[m.group(0)], text)
    text = re.sub(r"\b(?!wires\b)([a-z]+)\b", r"wires['\1']", text)
    return text

def part1():
    instructions = parse_input('input.txt')
    wires = {}
    for line in instructions:
        i, wire = line.split(' -> ')
        instruction = replace_bitwise(i)
        wires[wire] = eval(instruction, {}, {'wires': wires})
    print(f"Part 1: {wires['a']}")


if __name__ == '__main__':
    part1()
