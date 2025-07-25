#!/usr/bin/env python3

class Box:
    def __init__(self, l, w, h):
        self.l = int(l)
        self.w = int(w)
        self.h = int(h)
        self.sides = [
            self.l * self.w,
            self.w * self.h,
            self.h * self.l
        ]
        self.perimeters = [
            (2 * self.l) + (2 * self.w),
            (2 * self.w) + (2 * self.h),
            (2 * self.h) + (2 * self.l)
        ]

    def smallest_side(self):
        return min(self.sides)

    def needed_paper(self):
        return (2 * sum(self.sides)) + self.smallest_side()
    
    def smallest_perimeter(self):
        return min(self.perimeters)

    def bow_length(self):
        return self.l * self.w * self.h
    
    def needed_ribbon(self):
        return self.smallest_perimeter() + self.bow_length()

    def __str__(self):
        return f"{self.l} * {self.w} * {self.h}"

def parse_input(input_file = "input.txt"):
    boxes = []
    with open(input_file, 'r') as fin:
        for line in fin.readlines():
            l, w, h = line.strip().split("x")
            box = Box(l, w, h)
            boxes.append(box)
    return boxes

def part1():
    boxes = parse_input()
    total = 0
    for box in boxes:
        total += box.needed_paper()
    print(f"Part 1: {total}")

def part2():
    boxes = parse_input()
    total = 0
    for box in boxes:
        total += box.needed_ribbon()
    print(f"Part 2: {total}")

if __name__ == "__main__":
    part1()
    part2()