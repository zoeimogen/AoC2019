#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 9 solution'''

from typing import List, Tuple
from aoc2019 import intcode

Program = List[int]

def runpart1(program: Program) -> int:
    '''Run part one'''
    p = intcode.Program('standard', program, [1])
    return p.run()[0]

def runpart2(program: Program) -> int:
    '''Run part two'''
    p = intcode.Program('standard', program, [2])
    return p.run()[0]

def run() -> Tuple[int, int]:
    '''Main'''

    # Read program and put into data
    with open("inputs/day09.txt") as f:
        data = list(map(int, f.readline().split(',')))

    # Run the solution
    return(runpart1(data), runpart2(data))

if __name__ == '__main__':
    print(run())
