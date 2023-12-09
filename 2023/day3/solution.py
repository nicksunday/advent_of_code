#!/usr/bin/env python3

SYMBOLS = {'-', '+', '@', '&', '*', '/', '$', '=', '#', '%'}

def parse_input(file_name: str = 'input.txt') -> list:
    matrix = []
    with open(file_name, 'r', encoding='utf-8') as engine_schematic:
        for line in engine_schematic.readlines():
            matrix.append([c for c in line.strip()])
    return matrix


def get_numbers_and_coordinates(engine_matrix: list) -> list:
    number_coords = []
    for row, data in enumerate(engine_matrix):
        current = ''
        coordinates = tuple()
        for column, character in enumerate(data):
            if character in list(SYMBOLS) + ['.']:
                if current != '':
                    number_coords.append([coordinates, current])
                current = ''
                continue
            else:
                if current == '':
                    coordinates = (column, row)
                current = f"{current}{character}"
        if current != '':
            number_coords.append([coordinates, current])
    return number_coords


def symbols_above(number_matrix: list, coordinates: tuple, number: str) -> bool:
    # print(f"Checking ABOVE {number}")
    x = coordinates[0]
    y = coordinates[1]
    coords_to_check = []
    if y > 0:
        if x == 0:
            coords_to_check = [i for i in range(x, x + len(number) + 1)]
        elif x + len(number) == len(number_matrix[y - 1]):
            coords_to_check = [i for i in range(x - 1, x + len(number))]
        else:
            coords_to_check = [i for i in range(x - 1, x + len(number) + 1)]
        for i in coords_to_check:
            # print(x, len(number), x + len(number))
            # print(len(number_matrix[y - 1]), i)
            if number_matrix[y - 1][i] in SYMBOLS:
                return True
    return False


def symbols_left_right(number_matrix: list, coordinates: tuple, number: str) -> bool:
    # print(f"Checking LEFT/RIGHT {number}")
    x = coordinates[0]
    y = coordinates[1]
    if x > 0:
        if number_matrix[y][x - 1] in SYMBOLS:
            return True
    if x + len(number) != len(number_matrix[y]):
        if number_matrix[y][x + len(number)] in SYMBOLS:
            return True
    return False


def symbols_below(number_matrix: list, coordinates: tuple, number: str) -> bool:
    # print(f"Checking BELOW {number}")
    x = coordinates[0]
    y = coordinates[1]
    coords_to_check = []
    if y == len(number_matrix) - 1:
        return False
    else:
        if x == 0:
            coords_to_check = [i for i in range(x, x + len(number) + 1)]
        elif x + len(number) == len(number_matrix[y + 1]):
            coords_to_check = [i for i in range(x - 1, x + len(number))]
        else:
            coords_to_check = [i for i in range(x - 1, x + len(number) + 1)]
    for i in coords_to_check:
        if number_matrix[y + 1][i] in SYMBOLS:
            return True
    return False


def part1() -> None:
    total = 0
    engine_matrix = parse_input() # 'test2.txt') # 'example.txt')
    number_coords = get_numbers_and_coordinates(engine_matrix)
    # print(engine_matrix)
    for coordinates, number in number_coords:
        # print(coordinates, number)
        if symbols_above(engine_matrix, coordinates, number):
            # print(f"Found symbols above: {number}")
            total += int(number)
            continue
        if symbols_left_right(engine_matrix, coordinates, number):
            # print(f"Found symbols on the side of: {number}")
            total += int(number)
            continue
        if symbols_below(engine_matrix, coordinates, number):
            # print(f"Found symbols below: {number}")
            total += int(number)
            continue
    print(f"Part 1 Total: {total}")


def get_gear_coordinates(engine_matrix: list) -> list:
    gear_coords = []
    for row, data in enumerate(engine_matrix):
        coordinates = tuple()
        for column, character in enumerate(data):
            if character == '*':
                coordinates = (column, row)
                gear_coords.append(coordinates)
    return gear_coords


def part2() -> None:
    grand_total = 0
    engine_matrix = parse_input() # 'example.txt')
    gear_coords = get_gear_coordinates(engine_matrix)
    number_coords = get_numbers_and_coordinates(engine_matrix)
    for gear_coord in gear_coords:
        gear_parts = []
        gx = gear_coord[0]
        gy = gear_coord[1]
        for num_coord, number in number_coords:
            nx = num_coord[0]
            ny = num_coord[1]
            l = len(number)
            x_range = range(nx, nx + l)
            # print(x_range)
            for i in range(gx - 1, gx + 2):
                if i in x_range and gy - 1 <= ny <= gy + 1:
                    gear_parts.append(int(number))
                    break
        if len(gear_parts) == 2:
            grand_total += (gear_parts[0] * gear_parts[1])
    print(f"Part 2 Total: {grand_total}")

if __name__ == '__main__':
    part1()
    part2()
