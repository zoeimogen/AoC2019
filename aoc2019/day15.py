#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 15 solution'''

from collections import deque
import copy
from typing import List, Tuple, Dict, Deque, Any
import numpy
from aoc2019 import intcode

Program = List[int]
Grid = List[List[int]]
SHOW_GRID = False

def show_grid(grid: Grid, location: Tuple[int, int], steps: int, result: int) -> None:
    '''Shows the grid, in case you want to watch the game'''
    if not SHOW_GRID:
        return

    print("\033[0;0H")
    for x in grid:
        for y in x:
            # print(y)
            if y == 0:
                print(' ', end='')
            elif y == 1:
                print('#', end='')
            elif y == 2:
                print('.', end='')
            elif y == 3:
                print('o', end='')
            else:
                print('?', end='')
        print('')
    print(f"Location: {location}   Steps: {steps}   Result: {result}     ")

def walk_grid(program: Program) -> Tuple[int, Grid, Tuple[int, int]]:
    '''Generate a grid (Map) from the program, also finding the oxygen source'''
    grid = numpy.zeros((50, 50), int)
    pgm = intcode.Program('iterate', program)
    pgm.state['location'] = tuple([0, 0])
    pgm.state['steps'] = 0
    directions = [[0, 1, 0],
                  [1, -1, 0],
                  [2, 0, -1],
                  [3, 0, 1]]
    visited: List[Tuple[int, int]] = []
    # Keep a queue of program states, starting with the initial program
    queue = deque([pgm.state])
    while queue:
        pgmstate: Dict[str, Any] = queue.popleft()
        # Try every direction from our current state
        for d in directions:
            new_loc = (pgmstate['location'][0] + d[1],
                       pgmstate['location'][1] + d[2])
            # Skip locations we've already visited
            if new_loc not in visited:
                # Make a copy of our state
                pgm.state = copy.deepcopy(pgmstate)
                # Try the move
                pgm.state['inputs'] = [d[0]+1]
                result = pgm.run()[0]
                # Show the viewers what's going on, if requested.
                grid[new_loc[0]+25][new_loc[1]+25] = result + 1
                show_grid(grid, new_loc, pgm.state['steps'], result)
                if result == 2:
                    # Success!
                    steps = pgm.state['steps'] + 1
                    oxy = new_loc
                if result in (1, 2):
                    # We can move here, so add it to the queue of states to try
                    visited.append(new_loc)
                    pgm.state['location'] = new_loc
                    pgm.state['steps'] += 1
                    queue.append(pgm.state)

    return(steps, grid, oxy)

def runpart2(grid: Grid, oxy: Tuple[int, int]) -> int:
    '''Run part two'''
    directions = [[0, 1, 0],
                  [1, -1, 0],
                  [2, 0, -1],
                  [3, 0, 1]]

    queue: Deque[List[int]] = deque([[oxy[0], oxy[1], 0]])
    while queue:
        data: List[int] = queue.popleft()
        for d in directions:
            new_loc = (data[0] + d[1],
                       data[1] + d[2])
            if grid[new_loc[0]+25][new_loc[1]+25] == 2:
                grid[new_loc[0]+25][new_loc[1]+25] = 3
                queue.append([new_loc[0], new_loc[1], data[2] + 1])
                show_grid(grid, new_loc, data[2], 0)
    return data[2]

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day15.txt") as f:
        data = list(map(int, f.readline().split(',')))

    part1 = walk_grid(data)
    # Run the solution
    return(part1[0], runpart2(part1[1], part1[2]))

if __name__ == '__main__':
    print(run())
