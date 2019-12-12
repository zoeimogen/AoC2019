#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 2 solution'''

import copy
from typing import List, Tuple
from aoc2019.intcode import Program

Prg = List[int]

def verb_run(program: Prg, noun: int, verb: int) -> int:
    '''Run a program with a noun and a verb'''
    prg = copy.copy(program)
    prg[1] = noun
    prg[2] = verb
    p = Program('standard', prg)
    return p.run()[0]

def runpart2(program: Prg) -> int:
    '''Run part two'''
    for x in range(0, 100):
        for y in range(0, 100):
            if verb_run(program, x, y) == 19690720:
                return x*100 + y

    return 0 # Failed to find a solution

def run() -> Tuple[int, int]:
    '''Main'''

    # Read program and put into data
    with open("inputs/day02.txt") as f:
        data = list(map(int, f.readline().split(',')))

    # Run the solution
    part1 = verb_run(data, 12, 2)
    part2 = runpart2(data)
    return (part1, part2)

if __name__ == '__main__':
    print(run())
