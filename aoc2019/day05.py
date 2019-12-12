#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 5 solution'''

from typing import List, Tuple
from aoc2019 import intcode

Program = List[int]

def run() -> Tuple[int, int]:
    '''Main'''

    # Read program and put into data
    with open("inputs/day05.txt") as f:
        data: Program = list(map(int, f.readline().split(',')))

    # Run the solution
    p1 = intcode.Program('standard', data, inputs=[1])
    p2 = intcode.Program('standard', data, inputs=[5])

    return(p1.run()[-1], p2.run()[0])

if __name__ == '__main__':
    print(run())
