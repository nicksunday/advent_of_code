#!/usr/bin/env python3

from math import lcm

def parse_input(file_name: str = 'input.txt') -> tuple:
    nodes = {}
    with open(file_name, 'r', encoding='utf-8') as map:
        instructions, node_data = map.read().split('\n\n')
        for node in node_data.split('\n'):
            name, peers_data = node.split(' = ')
            peers = peers_data.removeprefix('(').removesuffix(')').split(', ')
            nodes[name] = {'L': peers[0], 'R': peers[1]}
    return (instructions, nodes)


def part1() -> int:
    steps = 0
    instructions, nodes = parse_input() # 'example2.txt')
    current_node = 'AAA'
    while current_node != 'ZZZ':
        for step in instructions:
            steps += 1
            current_node = nodes[current_node][step]
    return steps


#def process_node(nodes: dict, node: str, step: str, new_current_nodes: list) -> None:
 #   new_current_nodes.append(nodes[node][step])


def part2() -> int:
    steps_list = []
    instructions, nodes = parse_input() #'example3.txt')
    current_nodes = [node for node in nodes if node.endswith('A')]
    for node in current_nodes:
        current_node = node
        steps = 0
        while not current_node.endswith('Z'):
            for step in instructions:
                steps += 1
                current_node = nodes[current_node][step]
        steps_list.append(steps)
    total = 1
    for s in steps_list:
        total = lcm(s, total)
    return total


if __name__ == '__main__':
    print(f"Part 1 steps: {part1()}")
    print(f"Part 2 steps: {part2()}")