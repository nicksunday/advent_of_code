#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re

def part1():
    grid = np.zeros((1000, 1000), dtype=bool)

    def apply_instruction(instruction):
        # Parse the instruction
        parts = instruction.split()
        if parts[0] == "turn":
            action = parts[1]
            start = tuple(map(int, parts[2].split(',')))
            end = tuple(map(int, parts[4].split(',')))
        else:  # toggle
            action = "toggle"
            start = tuple(map(int, parts[1].split(',')))
            end = tuple(map(int, parts[3].split(',')))
        
        x1, y1 = start
        x2, y2 = end
        
        if action == "on":
            grid[y1:y2+1, x1:x2+1] = True
        elif action == "off":
            grid[y1:y2+1, x1:x2+1] = False
        elif action == "toggle":
            grid[y1:y2+1, x1:x2+1] = ~grid[y1:y2+1, x1:x2+1]
    
    def count_lights_on():
        return np.sum(grid)
    
    with open("input.txt") as f:
        for line in f:
            apply_instruction(line.strip())

    print("Part 1:", count_lights_on())

def part2():
    grid = np.zeros((1000, 1000), dtype=np.int64)

    pat = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')

    def apply_instruction(instr: str):
        m = pat.fullmatch(instr)
        if not m:
            return  # or raise

        action, x1, y1, x2, y2 = m.group(1, 2, 3, 4, 5)
        x1 = int(x1); y1 = int(y1); x2 = int(x2); y2 = int(y2)

        xs = slice(x1, x2 + 1)  # inclusive
        ys = slice(y1, y2 + 1)  # inclusive

        if action == "turn on":
            grid[ys, xs] += 1
        elif action == "turn off":
            view = grid[ys, xs]
            view[...] = np.maximum(view - 1, 0)
        else:  # toggle
            grid[ys, xs] += 2

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                apply_instruction(line)

    total_brightness = grid.sum()          # (or np.sum(grid))
    print("Part 2:", total_brightness)


if __name__ == "__main__":
    part1()
    part2()
