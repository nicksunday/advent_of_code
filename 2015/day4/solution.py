#!/usr/bin/env python3

import hashlib


def part1():
    secret_key = "bgvyzdsv"

    num = 0
    while True:
        num += 1
        secret_text = secret_key + str(num)
        md5_hash = hashlib.md5(secret_text.encode('utf-8'))
        md5 = md5_hash.hexdigest()
        if md5[:5] == "00000":
            return num

def part2():
    secret_key = "bgvyzdsv"

    num = 0
    while True:
        num += 1
        secret_text = secret_key + str(num)
        md5_hash = hashlib.md5(secret_text.encode('utf-8'))
        md5 = md5_hash.hexdigest()
        if md5[:6] == "000000":
            return num

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")