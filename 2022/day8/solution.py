#!/usr/bin/env python3

def parse_input(file_name: str = 'input.txt') -> list:
    matrix = []
    with open(file_name, 'r', encoding='utf-8') as grid:
        for line in grid.read().split('\n'):
            matrix.append([c for c in line])
    return matrix

def part1() -> int:
    visible = 0
    matrix = parse_input() #'example.txt')
    # Add top edge
    visible += len(matrix[0])
    # Add bottom edge
    visible += len(matrix[-1])
    # Add left edge
    visible += len(matrix) - 2
    # Add right edge
    visible += len(matrix) - 2
    for row, data in enumerate(matrix):
        for column, height in enumerate(data):
            if 0 < row < len(matrix) - 1:
                if 0 < column < len(data) - 1:
                    # Check all left
                    if (
                        max(data[:column]) < height or
                        max(data[column + 1:]) < height or
                        max(r[column] for r in matrix[:row]) < height or
                        max(r[column] for r in matrix[row + 1:]) < height
                    ):
                        visible += 1
    return visible


if __name__ == '__main__':
    print(f"Part 1 total: {part1()}")
