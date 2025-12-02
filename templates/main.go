package main

import (
	"fmt"
	"os"
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
	return 0
}

func part2(lines []string) int {
	return 0
}