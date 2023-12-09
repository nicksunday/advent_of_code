#!/usr/bin/env python3

def seed_dictionaries_part1(file_name: str = 'input.txt') -> tuple:
    seed_reference = {}
    almanac = {}
    with open(file_name, 'r', encoding='utf-8') as almanac_raw:
        current = ''
        for line in almanac_raw.readlines():
            if "seeds" in line:
                _, seeds_str = line.strip().split(': ')
                for seed in seeds_str.split():
                    seed_reference[int(seed)] = {}
            elif "map" in line:
                name = line.strip().split()[0]
                almanac[name] = []
                current = name
            elif line != '\n' and all(item.isnumeric() for item in line.strip().split()):
                dest_start, source_start, length = [int(i) for i in line.strip().split()]
                # dest = [i for i in range(dest_start, dest_start + length)]
                # source = [i for i in range(source_start, source_start + length)]
                dest = range(dest_start, dest_start + length)
                source = range(source_start, source_start + length)
                almanac.get(current).append({
                    "destination": dest,
                    "source": source
                })
    return (seed_reference, almanac)


def fill_seed_reference(seed_reference: dict, almanac: dict) -> dict:
    for seed in seed_reference:
        found = False
        for sts in almanac['seed-to-soil']:
            if seed in sts['source']:
                seed_map = sts['source'].index(seed)
                seed_reference[seed]["soil"] = sts['destination'][seed_map]
                found = True
                break
        if not found:
            seed_reference[seed]["soil"] = seed
    for seed in seed_reference:
        found = False
        soil = seed_reference[seed]['soil']
        for stf in almanac['soil-to-fertilizer']:
            if soil in stf['source']:
                seed_map = stf['source'].index(soil)
                seed_reference[seed]["fertilizer"] = stf['destination'][seed_map]
                found = True
                break
        if not found:
            seed_reference[seed]["fertilizer"] = soil
    for seed in seed_reference:
        found = False
        fertilizer = seed_reference[seed]['fertilizer']
        for ftw in almanac['fertilizer-to-water']:
            if seed_reference[seed]['fertilizer'] in ftw['source']:
                seed_map = ftw['source'].index(fertilizer)
                seed_reference[seed]["water"] = ftw['destination'][seed_map]
                found = True
                break
        if not found:
            seed_reference[seed]["water"] = fertilizer
    for seed in seed_reference:
        found = False
        water = seed_reference[seed]['water']
        for wtl in almanac['water-to-light']:
            if seed_reference[seed]['water'] in wtl['source']:
                seed_map = wtl['source'].index(water)
                seed_reference[seed]["light"] = wtl['destination'][seed_map]
                found = True
                break
        if not found:
            seed_reference[seed]["light"] = water
    for seed in seed_reference:
        found = False
        light = seed_reference[seed]['light']
        for ltt in almanac['light-to-temperature']:
            if light in ltt['source']:
                seed_map = ltt['source'].index(light)
                seed_reference[seed]["temperature"] = ltt['destination'][seed_map]
                found = True
                break
        if not found:
            seed_reference[seed]["temperature"] = light
    for seed in seed_reference:
        found = False
        temperature = seed_reference[seed]['temperature']
        for tth in almanac['temperature-to-humidity']:
            if temperature in tth['source']:
                seed_map = tth['source'].index(temperature)
                seed_reference[seed]["humidity"] = tth['destination'][seed_map]
                found = True
                break
        if not found:
            seed_reference[seed]["humidity"] = temperature
    for seed in seed_reference:
        found = False
        humidity = seed_reference[seed]['humidity']
        for htl in almanac['humidity-to-location']:
            if humidity in htl['source']:
                seed_map = htl['source'].index(humidity)
                seed_reference[seed]["location"] = htl['destination'][seed_map]
                found = True
                break
        if not found:
            seed_reference[seed]["location"] = humidity
    return seed_reference


def seed_dictionaries_part2(file_name: str = 'input.txt') -> tuple:
    # seed_reference = {}
    seed_reference = {}
    almanac = {}
    with open(file_name, 'r', encoding='utf-8') as almanac_raw:
        current = ''
        for line in almanac_raw.readlines():
            if "seeds" in line:
                _, seeds_str = line.strip().split(': ')
                seeds_list = [int(i) for i in seeds_str.split()]
                for seed_index in range(0, len(seeds_list), 2):
                    seed = seeds_list[seed_index]
                    span = seeds_list[seed_index + 1]
                    # seed_reference.update({seed: {} for seed in range(seed, seed + span)})
                    seed_reference.update({range(seed, seed + span): {}})
            elif "map" in line:
                name = line.strip().split()[0]
                almanac[name] = []
                current = name
            elif line != '\n' and all(item.isnumeric() for item in line.strip().split()):
                dest_start, source_start, length = [int(i) for i in line.strip().split()]
                # dest = [i for i in range(dest_start, dest_start + length)]
                # source = [i for i in range(source_start, source_start + length)]
                dest = range(dest_start, dest_start + length)
                source = range(source_start, source_start + length)
                almanac.get(current).append({
                    "destination": dest,
                    "source": source
                })
    return (seed_reference, almanac)


def fill_seed_reference_part2(seed_ranges: dict, almanac: dict) -> dict:
    seed_reference = {}
    for seed_range in seed_ranges:
        for seed in seed_range:
            found = False
            for sts in almanac['seed-to-soil']:
                if seed in sts['source']:
                    seed_map = sts['source'].index(seed)
                    seed_reference[seed]["soil"] = sts['destination'][seed_map]
                    found = True
                    break
            if not found:
                seed_reference[seed]["soil"] = seed
        for seed in seed_range:
            found = False
            soil = seed_reference[seed]['soil']
            for stf in almanac['soil-to-fertilizer']:
                if soil in stf['source']:
                    seed_map = stf['source'].index(soil)
                    seed_reference[seed]["fertilizer"] = stf['destination'][seed_map]
                    found = True
                    break
            if not found:
                seed_reference[seed]["fertilizer"] = soil
        for seed in seed_range:
            found = False
            fertilizer = seed_reference[seed]['fertilizer']
            for ftw in almanac['fertilizer-to-water']:
                if seed_reference[seed]['fertilizer'] in ftw['source']:
                    seed_map = ftw['source'].index(fertilizer)
                    seed_reference[seed]["water"] = ftw['destination'][seed_map]
                    found = True
                    break
            if not found:
                seed_reference[seed]["water"] = fertilizer
        for seed in seed_range:
            found = False
            water = seed_reference[seed]['water']
            for wtl in almanac['water-to-light']:
                if seed_reference[seed]['water'] in wtl['source']:
                    seed_map = wtl['source'].index(water)
                    seed_reference[seed]["light"] = wtl['destination'][seed_map]
                    found = True
                    break
            if not found:
                seed_reference[seed]["light"] = water
        for seed in seed_range:
            found = False
            light = seed_reference[seed]['light']
            for ltt in almanac['light-to-temperature']:
                if light in ltt['source']:
                    seed_map = ltt['source'].index(light)
                    seed_reference[seed]["temperature"] = ltt['destination'][seed_map]
                    found = True
                    break
            if not found:
                seed_reference[seed]["temperature"] = light
        for seed in seed_range:
            found = False
            temperature = seed_reference[seed]['temperature']
            for tth in almanac['temperature-to-humidity']:
                if temperature in tth['source']:
                    seed_map = tth['source'].index(temperature)
                    seed_reference[seed]["humidity"] = tth['destination'][seed_map]
                    found = True
                    break
            if not found:
                seed_reference[seed]["humidity"] = temperature
        for seed in seed_range:
            found = False
            humidity = seed_reference[seed]['humidity']
            for htl in almanac['humidity-to-location']:
                if humidity in htl['source']:
                    seed_map = htl['source'].index(humidity)
                    seed_reference[seed]["location"] = htl['destination'][seed_map]
                    found = True
                    break
            if not found:
                seed_reference[seed]["location"] = humidity
    return seed_reference


def part1() -> int:
    seed_reference, almanac = seed_dictionaries_part1() #'example.txt')
    complete_seed_reference = fill_seed_reference(seed_reference, almanac)
    # for seed in seed_reference: print(seed, seed_reference.get(seed))
    locations = [seed_reference[seed]['location'] for seed in complete_seed_reference]
    # print(locations)
    return min(locations)


def part2() -> int:
    seed_reference, almanac = seed_dictionaries_part2() # 'example.txt')
    complete_seed_reference = fill_seed_reference_part2(seed_reference, almanac)
    locations = [seed['location'] for seed in complete_seed_reference]
    return min(locations)
    #complete_seed_reference = fill_seed_reference(seed_reference, almanac)
    #locations = [seed_reference[seed]['location'] for seed in complete_seed_reference]
    # print(locations)
    #return min(locations)

if __name__ == '__main__':
    # print(f"Part 1 Location: {part1()}")
    print(f"Part 2 Location: {part2()}")