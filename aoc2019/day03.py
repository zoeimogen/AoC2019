#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 3 solution'''

import operator
from typing import Tuple, List
import numpy

GRIDSIZE = 20000

Grid = List[List[int]]
# Really Tuple[int, int, int, int] but mypy doesn't like map()
Coords = Tuple[int, ...] # x, y, distance, best match.

def follow(points: Grid, xy: Coords, c: str, manhattan: bool, comparison: bool) -> Coords:
    '''Follow a single instruction on the grid'''

    # Find the direction vector we need.
    if c[0] == 'U':
        direction = (0, 1, 1, 0)
    elif c[0] == 'R':
        direction = (1, 0, 1, 0)
    elif c[0] == 'D':
        direction = (0, -1, 1, 0)
    else:
        direction = (-1, 0, 1, 0)

    # Loop for the necessary distance
    for _ in range(0, int(c[1:])):
        # Take the step
        xy = tuple(map(operator.add, xy, direction))
        # If it's not a comparison run and we haven't been here yet, set the grid value
        if not comparison and points[xy[0]][xy[1]] == 0:
            points[xy[0]][xy[1]] = xy[2]
        # If is IS the comparison run and we've been here, check for match
        elif comparison and points[xy[0]][xy[1]] > 0:
            if manhattan:
                match = int(abs(xy[0] - GRIDSIZE / 2) + abs(xy[1] - GRIDSIZE / 2))
            else:
                match = points[xy[0]][xy[1]] + xy[2]
            if match < xy[3]:
                xy = (xy[0], xy[1], xy[2], match)
    return xy

def single_run(wire1: List[str], wire2: List[str], manhattan: bool) -> int:
    '''Complete an actual run'''
    # Set up the grid
    o = int(GRIDSIZE / 2)
    grid: Grid = numpy.zeros((GRIDSIZE, GRIDSIZE), dtype=int)

    # First pass - set the grid up with the first wire
    coords: Coords = (o, o, 0, 0)
    for cmd in wire1:
        coords = follow(grid, coords, cmd, False, False)

    # Second pass - find the answer based on Manhattan distance
    coords = (o, o, 0, 99999)
    for cmd in wire2:
        coords = follow(grid, coords, cmd, manhattan, True)

    return coords[3]

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day03.txt") as f:
        wire1 = f.readline().split(',')
        wire2 = f.readline().split(',')

    return(single_run(wire1, wire2, True),
           single_run(wire1, wire2, False))

if __name__ == '__main__':
    print(run())
