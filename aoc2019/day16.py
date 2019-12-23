#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 16 solution'''

from math import ceil

pattern = [0, 1, 0, -1]

def phase(sig, signallen):
    '''Perform a single phase calculation'''
    output = []
    for j in range(0, signallen):
        c = 0
        for (i, s) in enumerate(sig):
            c += s * pattern[(i+1) // (j+1) % 4]
        output.append(abs(c) % 10)
    return output

def cycle(sig, count) -> int:
    '''Cycle for part 1'''
    signallen = len(sig)
    for _ in range(0, count):
        sig = phase(sig, signallen)
    return int(''.join(map(str, sig[0:8])))

def cycle_part2(sig, count):
    '''Partial-grid cycle for part 2'''
    for _ in range(0, count):
        total = 0
        for i in range(len(sig) - 1, -1, -1):
            total += sig[i]
            sig[i] = total % 10
    return sig

def part2(sig, offset, length) -> int:
    '''Part 2 calculation - only use the part of the grid we need'''
    necessary_length = length - offset
    num_copies = ceil(necessary_length / len(sig))
    sig = sig * num_copies
    sig = sig[-necessary_length:]
    output = cycle_part2(sig, 100)

    message = ''.join(map(str, output[:8]))
    return int(message)

def run():
    '''Main'''
    with open("inputs/day16.txt") as f:
        data = f.readline().rstrip()

    inp = [int(i) for i in data]
    return (cycle(inp, 100), part2(inp, 5970537, 6500000))

if __name__ == '__main__':
    print(run())
