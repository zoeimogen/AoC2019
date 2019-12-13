#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 9 solution'''

from typing import List, Tuple
from aoc2019 import intcode

Program = List[int]

def runpart1(program: Program) -> int:
    '''Run part one'''
    p = intcode.Program('arcade', program)
    p.run()
    blocks = sum([len([y for y in x if y == 2]) for x in p.state['grid']])
    return blocks

def runpart2(program: Program) -> int:
    '''Run part two'''
    p = intcode.Program('arcade', program)
    p.state['pgm'][0] = 2
    # print(chr(27)+'[2j')
    # print('\033c')
    # print('\x1bc')
    # p.state['show_grid'] = True
    p.run()
    return p.state['score']

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day13.txt") as f:
        data = list(map(int, f.readline().split(',')))

    # Run the solution
    return(runpart1(data), runpart2(data))

if __name__ == '__main__':
    print(run())
