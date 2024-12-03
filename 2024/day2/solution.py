import argparse

def part1(input_file: str) -> None:
    safe_total = 0
    with open(input_file, 'r', encoding='utf-8') as reports:
        for line in reports.readlines():
            # print(line)
            levels = line.strip().split()
            # print(levels)
            ascending = False
            if int(levels[0]) < int(levels[1]):
                ascending = True
            safe = False
            for i in range(len(levels) - 1):
                # print(levels, end=' ')
                if ascending:
                    diff = int(levels[i + 1]) - int(levels[i])
                else:
                    diff = int(levels[i]) - int(levels[i + 1])
                if 1 <= diff <= 3:
                    safe = True
                else:
                    safe = False
                if not safe:
                    break
            # if not safe: print(levels, safe)
            if safe:
                safe_total += 1
    print(safe_total)

def part2(input_file: str) -> None:
    safe_total = 0
    queue = []
    with open(input_file, 'r', encoding='utf-8') as reports:
        for line in reports.readlines():
            # print(line)
            levels = [int(i) for i in line.strip().split()]
            a, d = 0, 0
            for i in range(len(levels) - 1):
                if levels[i] < levels[i + 1]:
                    a += 1
                if levels[i] > levels[i + 1]:
                    d += 1
                if a > d:
                    ascending = True
                else:
                    ascending = False
            queue.append(tuple((levels, ascending, True)))
            # queue.append(tuple((line.strip().split(), True)))
    
    while len(queue) > 0:
        levels, ascending, problem_dampener = queue.pop(0)
        # print(levels, problem_dampener)
        # ascending = False
        # if int(levels[0]) < int(levels[1]):
        #     ascending = True
        safe = True
        for i in range(len(levels) - 1):
            # diff = abs(int(levels[i + 1]) - int(levels[i]))
            if ascending:
                diff = int(levels[i + 1]) - int(levels[i])
            else:
                diff = int(levels[i]) - int(levels[i + 1])
            # if 1 <= diff <= 3:
            #     safe = True
            # else:  
            if not (1 <= diff <= 3):
                safe = False
                if problem_dampener:
                    # print("Dampening: ", levels, diff, levels[i + 1])
                    if ascending:
                        if i == 0 and levels[i] > levels[i + 1] and diff <= -3:
                            print("Damp 1")
                            _ = levels.pop(i + 1)
                        elif i == 0 and levels[i] > levels[i + 1]:
                            _ = levels.pop(i)
                        elif i == 0 and levels[i] < levels[i + 1] and diff > 3:
                            print("Damp 2")
                            _ = levels.pop(i)
                        elif levels[i] > levels[i + 1] and i == len(levels) - 2:
                            _ = levels.pop(i + 1)
                        elif levels[i] > levels[i + 1] and -1 >= diff >= -3:
                            print("Damp 3")
                            _ = levels.pop(i)
                        elif levels[i] < levels[i + 1] and -1 >= diff >= -3:
                            print("Damp 4")
                            _ = levels.pop(i + 1)
                        else:
                            print("Damp Default")
                            _ = levels.pop(i + 1)
                    else:
                        if levels[i] < levels[i + 1] and i == 0:
                            print("Damp 1")
                            _ = levels.pop(i)
                        elif levels[i] < levels[i + 1] and i == len(levels) - 2:
                            print("Damp 2")
                            _ = levels.pop(i + 1)
                        elif levels[i] < levels[i + 1] and diff <= -3:
                            print("Damp 3")
                            _ = levels.pop(i + 1)
                        elif levels[i] < levels[i + 1] and -1 >= diff >= -3:
                            print("Damp 4")
                            _ = levels.pop(i)
                        elif levels[i] > levels[i + 1] and diff > 3:
                            print("Damp 5")
                            _ = levels.pop(i + 1)
                        else:
                            print("Damp Default")
                            _ = levels.pop(i + 1)
                    print("Popped: ", _)
                    queue.append(tuple((levels, ascending, False)))
                break
            # if not safe:
            #     break
        if not safe: print(f"Ascending: {ascending}", levels, safe, problem_dampener, diff)
        if safe:
            safe_total += 1
    print(safe_total)

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    # parser.add_argument('--part', type=int, default=1)
    args = parser.parse_args()
    return args

def main():
    args = parse_input()
    part1(args.input_file)
    part2(args.input_file)

if __name__ == '__main__':
    main()