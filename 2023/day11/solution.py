#!/usr/bin/env python3

def parse_input(file_name: str = 'input.txt') -> list:
    matrix = []
    with open (file_name, 'r', encoding='utf-8') as galaxies:
        for row in galaxies.read().split('\n'):
            matrix.append([column for column in row])
    return matrix


def expand_galaxy(galaxy_matrix: list, expand_value: int = 2) -> list:
    rows_to_add = []
    columns_to_add = []
    for row, data in enumerate(galaxy_matrix):
        if all(column == '.' for column in data):
            rows_to_add.append(row)
    for column, _ in enumerate(galaxy_matrix[0]):
        if all(row[column] == '.' for row in galaxy_matrix):
            columns_to_add.append(column)
    for row in rows_to_add:
        #galaxy_matrix.insert(row, ['.' for i in range(len(galaxy_matrix[0]))])
        galaxy_matrix[row] = [str(expand_value) for i in range(len(galaxy_matrix[0]))]
    for row in galaxy_matrix:
        for column in columns_to_add:
            #row.insert(column, '.')
            row[column] = str(expand_value)
    return galaxy_matrix


def get_galaxy_coordinates(galaxy_matrix: list) -> list:
    coordinates = []
    for row, data in enumerate(galaxy_matrix):
        for column, character in enumerate(data):
            if character == '#':
                coordinates.append((column, row))
    return coordinates


def get_galaxy_pairs(galaxy_coordinates: list) -> set:
    pairs = set()
    for first_galaxy in galaxy_coordinates:
        for second_galaxy in galaxy_coordinates:
            if first_galaxy != second_galaxy:
                pair = tuple(sorted((first_galaxy, second_galaxy)))
                pairs.add(pair)
    return pairs


def get_total(galaxy_matrix: list, galaxy_pairs: list) -> int:
    grand_total = 0
    for first, second in galaxy_pairs:
        pair_total = 0
        x_range = sorted((first[0], second[0]))
        y_range = sorted((first[1], second[1]))
        for y in range(y_range[0], y_range[1]):
            if galaxy_matrix[y][min(x_range)].isnumeric():
                pair_total += int(galaxy_matrix[y][min(x_range)])
            else:
                pair_total += 1
        for x in range(x_range[0], x_range[1]):
            y_path = max(y_range)
            for y in range(y_range[0], y_range[1]):
                if not all(i.isnumeric() for i in galaxy_matrix[y]):
                    y_path = y
                    break
            if galaxy_matrix[y_path][x].isnumeric():
                pair_total += int(galaxy_matrix[max(y_range)][x])
            else:
                pair_total += 1
        grand_total += pair_total
        # print(f"{first},{second}: {pair_total}")
        # if sorted((first, second)) == sorted(((1, 5), (4, 9))):
        #     print(f"Testing {pair_total} == 9")
        #     assert pair_total == 9
    return grand_total


def part1() -> int:
    galaxy_matrix = parse_input() #'example.txt')
    expanded_galaxy = expand_galaxy(galaxy_matrix)
    galaxy_coordinates = get_galaxy_coordinates(expanded_galaxy)
    galaxy_pairs = get_galaxy_pairs(galaxy_coordinates)
    return get_total(galaxy_matrix, galaxy_pairs)


def part2() -> int:
    galaxy_matrix = parse_input() #'example.txt')
    expanded_galaxy = expand_galaxy(galaxy_matrix, 1000000)
    galaxy_coordinates = get_galaxy_coordinates(expanded_galaxy)
    galaxy_pairs = get_galaxy_pairs(galaxy_coordinates)
    return get_total(galaxy_matrix, galaxy_pairs)


if __name__ == '__main__':
    print(f"Part 1 total: {part1()}")
    print(f"Part 2 total: {part2()}")
