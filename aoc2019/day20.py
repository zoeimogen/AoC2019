#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 20 solution'''

import string
from collections import defaultdict, deque
import copy

def load_data(filename): # pylint: disable=too-many-branches,too-many-locals
    '''Load grid data from file'''
    portals = defaultdict(list)

    with open(filename) as f:
        grid = []
        for line in f:
            grid.append(line.rstrip() + '  ')

    for (y, l) in enumerate(grid):
        for (x, c) in enumerate(l):
            if c in string.ascii_uppercase:
                if y > 0 and grid[y-1][x] == '.':
                    # Enter portal from above
                    tag = c + grid[y+1][x]
                    if y == len(grid) - 2:
                        outer = -1
                    else:
                        outer = 1
                    portals[tag].append((y, x, y-1, x, outer))
                elif y < len(grid)-1 and grid[y+1][x] == '.':
                    # Enter portal from below
                    tag = grid[y-1][x] + c
                    if y == 1:
                        outer = -1
                    else:
                        outer = 1
                    portals[tag].append((y, x, y+1, x, outer))
                elif x > 0 and grid[y][x-1] == '.':
                    # Enter portal from left
                    tag = c + grid[y][x+1]
                    if x == len(grid[y]) - 4:
                        outer = -1
                    else:
                        outer = 1
                    portals[tag].append((y, x, y, x-1, outer))
                elif x < len(grid[y]) and grid[y][x+1] == '.':
                    # Enter portal from right
                    tag = grid[y][x-1] + c
                    if x == 1:
                        outer = -1
                    else:
                        outer = 1
                    portals[tag].append((y, x, y, x+1, outer))

    portals2 = {}

    for p in portals:
        pv = portals[p]
        if len(pv) == 2:
            portals2[(pv[0][0], pv[0][1])] = (pv[1][2], pv[1][3], pv[0][4], p)
            portals2[(pv[1][0], pv[1][1])] = (pv[0][2], pv[0][3], pv[1][4], p)

    start = (portals['AA'][0][2], portals['AA'][0][3])
    target = (portals['ZZ'][0][2], portals['ZZ'][0][3])
    return (grid, portals2, start, target)

def find_route(grid, portals, start, target):
    '''Find a route through the grid using the portals'''
    queue = deque([(1, start[0], start[1])])

    while queue:
        state = queue.popleft()
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            loc = (state[1] + d[0],
                   state[2] + d[1])
            loc = portals.get(loc, loc)
            if grid[loc[0]][loc[1]] != '.':
                continue
            if loc == target:
                return state[0]
            grid[loc[0]] = str(grid[loc[0]][:loc[1]]) + 'X' + str(grid[loc[0]][loc[1]+1:])
            queue.append((state[0]+1, loc[0], loc[1]))

def find_multilayer_route(grid, portals, start, target):
    '''Find a route through the grid using the portals'''
    queue = deque([(1, start[0], start[1], 0)])
    grids = [copy.copy(grid)]

    while queue:
        state = queue.popleft()
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            loc = (state[1] + d[0],
                   state[2] + d[1],
                   state[3])
            # print((loc[0], loc[1]))
            if (loc[0], loc[1]) in portals:
                # print(f"Possible portal found at {loc}")
                loc = (portals[(loc[0], loc[1])][0],
                       portals[(loc[0], loc[1])][1],
                       state[3] + portals[(loc[0], loc[1])][2])
                if loc[2] < 0 or loc[2] > 100:
                    # print(f"Skipping, went to level {loc[2]}")
                    continue
                if loc[2] not in grids:
                    # print("Expanding grid")
                    grids.append(copy.copy(grid))
            if grids[loc[2]][loc[0]][loc[1]] != '.':
                continue
            if (loc[0], loc[1]) == target and loc[2] == 0:
                return state[0]
            grids[loc[2]][loc[0]] = (str(grids[loc[2]][loc[0]][:loc[1]]) +
                                     'X' + str(grids[loc[2]][loc[0]][loc[1]+1:]))
            queue.append((state[0]+1, loc[0], loc[1], loc[2]))

def run():
    '''Main'''
    (grid, portals, start, target) = load_data("inputs/day20.txt")
    part1 = find_route(copy.copy(grid), portals, start, target)
    part2 = find_multilayer_route(grid, portals, start, target)
    return(part1, part2)

if __name__ == '__main__':
    print(run())
