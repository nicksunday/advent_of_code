package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

var debugMode bool = false

func debugPrint(format string, args ...interface{}) {
	if debugMode {
		fmt.Printf("[DEBUG] "+format+"\n", args...)
	}
}

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
	ans := 0
	var joltages []int

	for bank_idx, bank := range lines {
		max_bat := -1
		max_idx := -1
		second_bat := -1
		for idx, r := range bank {
			battery := int(r - '0')
			if battery > max_bat && idx < len(bank)-1 {
				max_bat = battery
				max_idx = idx
				second_bat = -1

			} else if battery > second_bat && idx > max_idx && max_bat > 0 {
				second_bat = battery
			}
		}
		jolt, err := strconv.Atoi(fmt.Sprintf("%d%d", max_bat, second_bat))
		if err != nil {
			panic(err)
		}
		debugPrint("Bank %d: %d\n", bank_idx, jolt)
		joltages = append(joltages, jolt)
	}

	for _, joltage := range joltages {
		ans += joltage
	}

	return ans
}

func part2(lines []string) int {
	ans := 0
	var joltages []int

	for bank_idx, bank := range lines {
		var bank_list []int
		for idx, r := range bank {
			battery := int(r - '0')

			remaining := len(bank) - idx - 1

			for len(bank_list) > 0 &&
				bank_list[len(bank_list)-1] < battery &&
				(len(bank_list)-1+remaining+1) >= 12 {
				bank_list = bank_list[:len(bank_list)-1]
			}

			if len(bank_list) < 12 {
				bank_list = append(bank_list, battery)
			}
		}

		var sb strings.Builder
		for _, b := range bank_list {
			sb.WriteString(strconv.Itoa(b))
		}
		jolt, err := strconv.Atoi(sb.String())
		if err != nil {
			panic(err)
		}
		debugPrint("Bank %d: %d\n", bank_idx, jolt)
		joltages = append(joltages, jolt)
	}

	for _, joltage := range joltages {
		ans += joltage
	}

	return ans
}
