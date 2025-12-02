import sys


def main():
    input_file = "input.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1] + ".input.txt"

    with open(input_file) as f:
        lines = f.read().strip().split("\n")

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


def part1(lines: list[str]) -> int:
    return 0


def part2(lines: list[str]) -> int:
    return 0


if __name__ == "__main__":
    main()
