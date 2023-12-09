#!/usr/bin/env python3
"""
Advent of Code Day 2
"""

def parse_input() -> dict:
    """ Converts the input into a parsable dict  """
    game_dict = {}
    with open('input.txt', 'r', encoding='utf-8') as cube_games:
        for line in cube_games.readlines():
            game, data = line.strip().split(': ')
            pulls_list = []
            for pull in data.split('; '):
                cubes = pull.split(', ')
                pull_dict = {}
                for cube in cubes:
                    number, color = cube.split(' ')
                    pull_dict[color] = number
                pulls_list.append(pull_dict)
            game_number = game.split(' ')[-1].strip()
            game_dict[game_number] = pulls_list
    return game_dict


def part1() -> None:
    """ main function """
    game_dict = parse_input()
    valid_games = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    total = 0
    for game, pulls in game_dict.items():
        valid = True
        for pull in pulls:
            for color in valid_games.keys():
                if int(pull.get(color, 0)) > int(valid_games.get(color)):
                    valid = False
        if valid:
            total += int(game)
    print(total)


def main() -> None:
    """ main function """
    game_dict = parse_input()
    total = 0
    for game, pulls in game_dict.items():
        min_colors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for pull in pulls:
            for color in min_colors.keys():
                if int(pull.get(color, 0)) > int(min_colors.get(color)):
                    min_colors[color] = int(pull.get(color))
        power = min_colors.get('red') * min_colors.get('green') * min_colors.get('blue')
        total += power
    print(total)


if __name__ == '__main__':
    main()
