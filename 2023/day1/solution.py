#!/usr/bin/env python3
"""
Advent of Code Day 1
"""

def main() -> None:
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    
    sum = 0
    with open('input.txt', 'r', encoding='utf-8') as calibration_file:
    # Part 1
    #     for line in calibration_file.readlines():
    #         for character in line:
    #             if character.isnumeric():
    #                 first_number = character
    #                 break
    #         for character in line[::-1]:
    #             if character.isnumeric():
    #                 last_number = character
    #                 break
    #         calibration_value = int(f"{first_number}{last_number}")
    #         sum += calibration_value
        for line in calibration_file.readlines():
            line_numbers = []
            for index, character in enumerate(line):
                if character.isnumeric():
                    line_numbers.append(character)
                else:
                    for name, value in numbers.items():
                        if line[index: index + len(name)] == name:
                            line_numbers.append(value)
                            break
            line_two_digit_num = int(f"{line_numbers[0]}{line_numbers[-1]}")
            sum += line_two_digit_num
    
    print(sum)


if __name__ == '__main__':
    main()
