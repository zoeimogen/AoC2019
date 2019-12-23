#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 19 solution'''

import copy
from typing import List, Tuple
from aoc2019 import intcode

Program = List[int]

def run_part1(data):
    '''Solve part 1'''
    count = 0
    for x in range(0, 50):
        for y in range(0, 50):
            pgm = intcode.Program('normal', copy.copy(data), [x, y])
            output = pgm.run()[0]
            if output == 1:
                count += 1

    return count

def run_part2(data):
    '''Solve part 2'''
    x = 5
    last_y_start = 0
    last_y_end = 0
    results = {}
    while True:
        line = ""
        y = last_y_start
        triggered = 0
        count = 0
        while True:
            pgm = intcode.Program('normal', copy.copy(data), [x, y])
            output = pgm.run()[0]
            if output == 1:
                line += '#'
                if triggered == 0:
                    triggered = 1
                    last_y_start = y
                    if last_y_end > y:
                        y = last_y_end-1
            elif triggered == 0:
                line += '.'
            else:
                line += '.'
                results[x] = (last_y_start, y-1)
                last_y_end = y-1
                break
            y += 1
        if x - 99 in results:
            if results[x-99][1] >= last_y_start + 99:
                return 10000 * (x-99) + last_y_start
        x += 1

    print(results)
    return count

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day19.txt") as f:
        data = list(map(int, f.readline().split(',')))

    return(run_part1(data), run_part2(data))

if __name__ == '__main__':
    print(run())
