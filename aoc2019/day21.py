#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 21 solution'''

import copy
from typing import Tuple
from aoc2019 import intcode

def run_robot(pgm, robot):
    '''Run a program for a robot'''
    inp = []
    for line in robot:
        for x in line:
            inp.append(ord(x))
        inp.append(10)
    pgm = intcode.Program('iterate', pgm, inp)
    while pgm.state['ptr'] != -1:
        output = pgm.run()[0]
        if output > 256:
            return output
        # else:
        #     print(chr(output), end='')

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day21.txt") as f:
        data = list(map(int, f.readline().split(',')))

    robot = ['NOT C J',
             'NOT B T',
             'OR T J',
             'NOT A T',
             'OR T J',
             'AND D J',
             'WALK']

    part1 = run_robot(copy.copy(data), robot)

    robot = ['NOT C J',
             'NOT B T',
             'OR T J',
             'NOT A T',
             'OR T J',
             'AND D J',
             'NOT E T',
             'NOT T T',
             'OR H T',
             'AND T J',
             'RUN']

    part2 = run_robot(copy.copy(data), robot)

    return(part1, part2)

if __name__ == '__main__':
    print(run())
