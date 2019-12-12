#!/usr/bin/env python3
# pylint: disable=invalid-name,consider-using-enumerate
'''Advent of Code 2019 Day 11 solution'''

from typing import List, Tuple
from aoc2019 import intcode

Program = List[int]
Grid = List[List[int]]

def run() -> Tuple[int, str]:
    '''Main'''

    # Read program and put into data
    with open("inputs/day11.txt") as f:
        data: Program = list(map(int, f.readline().split(',')))

    # Run the solution
    pgm = intcode.Program('robot', data)
    pgm.run()
    grid: Grid = pgm.state['grid']

    count = 0
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            if grid[y][x]:
                count += 1

    pgm = intcode.Program('robot', data)
    pgm.state['grid'][50][50] = 2
    pgm.run()
    grid = pgm.state['grid']

    part2 = ''
    for x in range(0, len(grid)):
        if sum(grid[x]):
            for y in range(0, len(grid[x])):
                if grid[x][y] == 2:
                    part2 += '#'
                else:
                    part2 += ' '
            part2 += '\n'

    return(count, part2)

if __name__ == '__main__':
    print(run())
