package main

import (
	"fmt"
	"os"
	"slices"
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

func createWarhouse(lines []string) [][]string {
	var warehouse [][]string

	for _, line := range lines {
		if len(line) != len([]rune(line)) {
			fmt.Println(len(line), len([]rune(line)))
		}
		row := make([]string, len(line))
		for i := 0; i < len(line); i++ {
			row[i] = string(line[i])
		}
		warehouse = append(warehouse, row)
	}
	return warehouse
}

func checkNeighbors(matrix [][]string, x, y int) int {
	neighbors := 0
	// Same row
	// Left (-1, 0)
	if x > 0 && matrix[y][x-1] == "@" {
		neighbors++
	}
	// Right (+1, 0)
	if x < len(matrix[y])-1 && matrix[y][x+1] == "@" {
		neighbors++
	}

	// Previous Row
	if y > 0 {
		// Diag Left (-1, -1)
		if x > 0 && matrix[y-1][x-1] == "@" {
			neighbors++
		}
		// Above (0, -1)
		if matrix[y-1][x] == "@" {
			neighbors++
		}
		// Diag Right (+1, -1)
		if x < len(matrix[y-1])-1 && matrix[y-1][x+1] == "@" {
			neighbors++
		}
	}

	// Next Row
	if y < len(matrix)-1 {
		// Diag Left (-1, +1)
		if x > 0 && matrix[y+1][x-1] == "@" {
			neighbors++
		}
		// Below (0, +1)
		if matrix[y+1][x] == "@" {
			neighbors++
		}
		// Diag Right (+1, +1)
		if x < len(matrix[y+1])-1 && matrix[y+1][x+1] == "@" {
			neighbors++
		}
	}
	return neighbors
}

func part1(lines []string) int {
	reachable := 0
	warehouse := createWarhouse(lines)

	for y, row := range warehouse {
		for x, gridItem := range row {
			if gridItem == "@" {
				neighbors := checkNeighbors(warehouse, x, y)
				if neighbors < 4 {
					reachable++
				}
			}
		}
	}
	return reachable
}

func part2(lines []string) int {
	removable := 0
	warehouse := createWarhouse(lines)

	for {
		timeout := 140
		for y, row := range warehouse {
			lastCount := removable
			if slices.Contains(row, "@") {
				for x, gridItem := range row {
					if gridItem == "@" {
						neighbors := checkNeighbors(warehouse, x, y)
						if neighbors < 4 {
							removable++
							warehouse[y][x] = "."
						}
					}
				}
			}
			if lastCount == removable {
				timeout--
			}
		}
		if timeout <= 0 {
			break
		}
	}
	return removable
}
