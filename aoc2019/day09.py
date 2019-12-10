#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 2 solution'''

import copy
from typing import List, Tuple
import numpy
from aoc2019.intcode import runprg

Program = List[int]

def runpart1(program: Program) -> int:
    '''Run part one'''
    prg = copy.copy(program)
    prg.extend((map(int, numpy.zeros(1000))))
    result = runprg(prg, [1])
    return result

def runpart2(program: Program) -> int:
    '''Run part two'''
    prg = copy.copy(program)
    prg.extend((map(int, numpy.zeros(1000))))
    result = runprg(prg, [2])
    return result

def run() -> Tuple[int, int]:
    '''Main'''

    # Read program and put into data
    with open("inputs/day09.txt") as f:
        data = list(map(int, f.readline().split(',')))

    # Run the solution
    part1 = runpart1(data)
    part2 = runpart2(data)
    return (part1, part2)

if __name__ == '__main__':
    print(run())
