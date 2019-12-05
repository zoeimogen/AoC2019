#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 5 solution'''

import copy
from aoc2019.intcode import runprg

def run():
    '''Main'''

    # Read program and put into data
    with open("inputs/day05.txt") as f:
        data = list(map(int, f.readline().split(',')))

    # Run the solution
    prg = copy.copy(data)
    part1 = runprg(prg, 1)
    part2 = runprg(data, 5)

    return(part1, part2)

if __name__ == '__main__':
    print(run())
