package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	inputFile := "input.txt"
	if len(os.Args) > 1 {
		inputFile = os.Args[1] + ".input.txt"
	}

	data, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	fmt.Println("Part 1:", part1(lines))
	fmt.Println("Part 2:", part2(lines))
}

func part1(lines []string) int {
	var ans int = 0
	var dial int = 50

	for _, line := range lines {
		direction := string(line[0])
		number, err := strconv.Atoi(string(line[1:]))
		if err != nil {
			panic(err)
		}
		if direction == "L" {
			dial = dial - number
		} else {
			dial = dial + number
		}
		if dial%100 == 0 {
			ans += 1
		}
	}

	return ans
}

func part2(lines []string) int {
	var ans int = 0
	var dial int = 50

	for _, line := range lines {
		var direction int
		if string(line[0]) == "L" {
			direction = -1
		} else {
			direction = 1
		}
		number, err := strconv.Atoi(string(line[1:]))
		if err != nil {
			panic(err)
		}
		freespins := number / 100
		number = number % 100
		ans += freespins
		dial = dial + (direction * number)
		if dial != 0 && (dial <= 0 || dial >= 100) {
			ans += 1
		}
		dial = dial % 100
	}
	return ans
}
