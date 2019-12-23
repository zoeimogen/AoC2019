#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 17 solution'''

import copy
from typing import List, Tuple
from aoc2019 import intcode

Program = List[int]

def find_crossover(grid) -> int:
    '''Find crossover alignment'''
    alignment = 0

    for a, x in enumerate(grid):
        for b, _ in enumerate(x):
            try:
                if (grid[a][b] == 35 and
                        grid[a-1][b] == 35 and
                        grid[a+1][b] == 35 and
                        grid[a][b+1] == 35 and
                        grid[a][b-1] == 35):
                    alignment += a*b
            except IndexError:
                pass

    return alignment

def run_part1(data):
    '''Solve part 1'''
    pgm = intcode.Program('iterate', data)
    grid = []
    line = []
    while True:
        output = pgm.run()[0]
        if pgm.state['ptr'] == -1:
            break
        if output == 10:
            grid.append(copy.copy(line))
            line = []
        else:
            line.append(output)

    return find_crossover(grid)

def run_part2(data):
    '''Solve part 2'''

    # Solution figured out by hand, as the problem is relatively simple
    robot = ['A,B,A,C,A,C,B,C,C,B',
             'L,4,L,4,L,10,R,4',
             'R,4,L,4,L,4,R,8,R,10',
             'R,4,L,10,R,10',
             'y']
    inp = []
    for line in robot:
        for x in line:
            inp.append(ord(x))
        inp.append(10)
    pgm = intcode.Program('iterate', data, inp)
    pgm.state['pgm'][0] = 2
    while pgm.state['ptr'] != -1:
        output = pgm.run()[0]
        if output > 256:
            return output
        # else:
        #     print(chr(output), end='')

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day17.txt") as f:
        data = list(map(int, f.readline().split(',')))

    return(run_part1(data), run_part2(data))

if __name__ == '__main__':
    print(run())
