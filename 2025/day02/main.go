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
	lines := strings.Split(strings.TrimSpace(string(data)), ",")

	fmt.Println("Part 1:", part1(lines))
	fmt.Println("Part 2:", part2(lines))
}

func part1(lines []string) int {
	var invalid_ids []int

	for _, line := range lines {
		id_range := strings.Split(line, "-")
		start, err := strconv.Atoi(string(id_range[0]))
		if err != nil {
			panic(err)
		}
		end, err := strconv.Atoi(string(id_range[1]))
		if err != nil {
			panic(err)
		}

		id_list := make([]int, end-start+1)
		for i := range id_list {
			curr_id := i + start
			curr_id_str := strconv.Itoa(curr_id)
			if len(curr_id_str)%2 == 0 {
				half := len(curr_id_str) / 2
				if curr_id_str[:half] == curr_id_str[half:] {
					invalid_ids = append(invalid_ids, curr_id)
				}
			}
		}
	}
	total := 0
	for _, id := range invalid_ids {
		total += id
	}
	return total
}

func isRepeated(s string) bool {
	if len(s) == 0 {
		return false
	}

	doubled := s + s
	// Slice off the first and last character so it can’t match trivially
	searchSpace := doubled[1 : len(doubled)-1]
	return strings.Contains(searchSpace, s)
}

func part2(lines []string) int {
	var invalid_ids []int

	for _, line := range lines {
		id_range := strings.Split(line, "-")
		start, err := strconv.Atoi(string(id_range[0]))
		if err != nil {
			panic(err)
		}
		end, err := strconv.Atoi(string(id_range[1]))
		if err != nil {
			panic(err)
		}

		id_list := make([]int, end-start+1)
		for i := range id_list {
			curr_id := i + start
			curr_id_str := strconv.Itoa(curr_id)
			if isRepeated(curr_id_str) {
				invalid_ids = append(invalid_ids, curr_id)
			}
		}
	}
	total := 0
	for _, id := range invalid_ids {
		total += id
	}
	return total
}
