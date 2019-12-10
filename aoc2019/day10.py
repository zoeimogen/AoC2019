#!/usr/bin/env python3
# pylint: disable=invalid-name, consider-using-enumerate, chained-comparison
'''Advent of Code 2019 Day 10 solution
   https://adventofcode.com/2019/day/10'''

import math
from collections import defaultdict
from typing import List, Tuple, Dict

Grid = List[str]
GridAngles = Dict[float, Dict[float, Tuple[int, int]]]

def sign_of(x: int) -> int:
    '''Returns 1 or -1 depending on the sign of the input'''
    if x >= 0:
        return 1
    return -1

def check_visible(x: int, y: int, a: int, b: int, grid: Grid) -> bool:
    '''Check if a, b is visible from x, y'''
    x_offset = a - x
    y_offset = b - y

    # Count from a to x...
    for c in range(1, abs(x_offset)):
        # ...and if this x coordinate (c) intersects an exact square...
        if (y_offset * c / x_offset) % 1 == 0:
            e = x + c*sign_of(x_offset)
            f = y + sign_of(x_offset)*int(y_offset * c / x_offset)
            # ...check if our line of site is blocked, and return False if so.
            if grid[f][e] == '#':
                return False

    # Repeating the count from b to y is the lazy way of handling the case where the offset is zero
    for d in range(1, abs(y_offset)):
        if (x_offset * d / y_offset) % 1 == 0:
            e = x + sign_of(y_offset)*int(x_offset * d / y_offset)
            f = y + d*sign_of(y_offset)
            if grid[f][e] == '#':
                return False

    return True

def count_visible(x: int, y: int, grid: Grid) -> int:
    '''Count the number of visible asteroids in the grid from x, y'''
    count = 0

    # Loop over the entire grid (a, b)...
    for a in range(0, len(grid[0])):
        for b in range(0, len(grid)):
            # ...finding just the asteroids, and ignoring the source...
            if not (a == x and b == y) and grid[b][a] == '#':
                # ...checking if a, b is visible from x, y.
                if check_visible(x, y, a, b, grid):
                    count += 1
    return count

def find_best_asteroid(grid: Grid) -> Tuple[int, int, int]:
    '''Solve Part 1 - find the asteroid that can see the most other asteroids'''
    best_location = (0, 0, 0)

    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            if grid[y][x] == '#':
                count = count_visible(x, y, grid)
                if count > best_location[2]:
                    best_location = (x, y, count)

    return best_location

def grid_angle(x: int, y: int) -> float:
    '''Get the angle of a pair of offsets. Returns radians.'''
    if x >= 0 and y > 0:
        return math.atan(x / y)

    if x > 0 and y <= 0:
        return math.pi/2 + math.atan(abs(y)/x)

    if x <= 0 and y < 0:
        return math.pi + math.atan(abs(x)/abs(y))

    return math.pi*1.5 + math.atan(y/abs(x))

def all_grid_angles(grid: Grid, best_location: Tuple[int, int, int]) -> GridAngles:
    '''Calculate the angle and distance of every grid square with an asteroid in it'''

    # This is a dict of angles, each containing a dict of distances.
    grid_angles: GridAngles = defaultdict(dict)

    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            # Skip the sensor location
            if not (x == best_location[0] and y == best_location[1]):
                if grid[y][x] == '#':
                    # No point square rooting this.
                    distance = abs(best_location[0] - x)**2 + abs(best_location[1] - y)**2
                    # Note angle calculation handles x and y differently - zero angle is
                    # negative x offset, positive y.
                    grid_angles[grid_angle(x - best_location[0],
                                           best_location[1] - y)][distance] = (x, y)

    return grid_angles

def destroy_asteroids(ga: GridAngles) -> List[Tuple[int, int]]:
    '''Return a list of the asteroids in the order they are destroyed'''
    asteroids: List[Tuple[int, int]] = []

    # At this point, we have a dict with the angle to every asteroid in the grid. We can just
    # sort that dict by angle and destroy the asteroids one by one. If there's more than one
    # asteroid at an angle, we only destroy the first one.
    while ga:
        for k in sorted(ga.keys()):
            j = sorted(ga[k].keys())[0]
            asteroids.append(ga[k][j])
            del ga[k][j]
            if not ga[k]:
                del ga[k]

    return asteroids

def run() -> Tuple[int, int]:
    '''Main'''
    grid: Grid = []
    with open("inputs/day10.txt") as f:
        for line in f:
            grid.append(line.rstrip())

    part1 = find_best_asteroid(grid)
    grid_angles = all_grid_angles(grid, part1)
    part2 = destroy_asteroids(grid_angles)
    return(part1[2], part2[199][0] * 100 + part2[199][1])

if __name__ == '__main__':
    print(run())
