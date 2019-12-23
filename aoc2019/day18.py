#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 18 solution'''

import string
from collections import deque
import copy

def load_data(data):
    '''Load grid data from file'''
    key_count = 0

    grid = []
    for line in data:
        if '@' in line:
            start = (len(grid), line.index('@'))
        key_count += len([c for c in line if c in string.ascii_lowercase])
        grid.append(line.rstrip() + '  ')

    return (grid, start, key_count)

def try_location(grids, loc, state):
    '''Test a location to see if it results in a valid state'''
    got_keys = state[1]
    if grids[got_keys][loc[0]][loc[1]] == '#':
        return None

    if (grids[got_keys][loc[0]][loc[1]] in string.ascii_uppercase
            and grids[got_keys][loc[0]][loc[1]] not in got_keys):
        return None

    if (grids[got_keys][loc[0]][loc[1]] in string.ascii_lowercase
            and grids[got_keys][loc[0]][loc[1]].upper() not in got_keys):
        got_keys = ''.join(sorted(got_keys + grids[got_keys][loc[0]][loc[1]].upper()))

    if got_keys not in grids:
        grids[got_keys] = copy.copy(grids['-'])

    grids[got_keys][loc[0]] = (str(grids[got_keys][loc[0]][:loc[1]]) +
                               '#' + str(grids[got_keys][loc[0]][loc[1]+1:]))

    return (state[0] + 1, got_keys, loc[0], loc[1])

def find_route(grid, start, key_count):
    '''Find a route through the map'''
    queue = deque([(0, '', start[0], start[1])])
    grids = {'': copy.copy(grid),
             '-': copy.copy(grid)}

    while queue:
        state = queue.popleft()
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_state = try_location(grids,
                                     (state[2] + d[0],
                                      state[3] + d[1]),
                                     state)

            if new_state is not None:
                if len(new_state[1]) == key_count:
                    return new_state[0]
                queue.append(new_state)
    return -1

def set_grid(grid, y, x, val):
    '''Set value of a grid square'''
    grid[y] = str(grid[y][:x]) + val + str(grid[y][x+1:])

def try_location_p2(grids, robot, loc, state):
    '''Test a location to see if it results in a valid state'''
    got_keys = state[1]
    if grids[got_keys][loc[0]][loc[1]] == '#':
        return None

    if (grids[got_keys][loc[0]][loc[1]] in string.ascii_uppercase
            and grids[got_keys][loc[0]][loc[1]] not in got_keys):
        return None

    if (grids[got_keys][loc[0]][loc[1]] in string.ascii_lowercase
            and grids[got_keys][loc[0]][loc[1]].upper() not in got_keys):
        got_keys = ''.join(sorted(got_keys + grids[got_keys][loc[0]][loc[1]].upper()))

    if got_keys not in grids:
        grids[got_keys] = copy.copy(grids['-'])

    set_grid(grids[got_keys], loc[0], loc[1], '#')
    new_robots = copy.copy(state[2])
    new_robots[robot] = (loc[0], loc[1])

    return (state[0] + 1, got_keys, new_robots)

def find_route_part2(grid, start, key_count):
    '''Find a route through the map'''
    set_grid(grid, start[0]-1, start[1]-1, '#')
    set_grid(grid, start[0]-1, start[1], '#')
    set_grid(grid, start[0]-1, start[1]+1, '#')
    set_grid(grid, start[0], start[1]-1, '#')
    set_grid(grid, start[0], start[1], '#')
    set_grid(grid, start[0], start[1]+1, '#')
    set_grid(grid, start[0]+1, start[1]-1, '#')
    set_grid(grid, start[0]+1, start[1], '#')
    set_grid(grid, start[0]+1, start[1]+1, '#')

    queue = deque([(0, '', [(start[0]-1, start[1]-1),
                            (start[0]-1, start[1]+1),
                            (start[0]+1, start[1]-1),
                            (start[0]+1, start[1]+1)])])
    grids = {'': copy.copy(grid),
             '-': copy.copy(grid)}

    while queue:
        state = queue.popleft()
        for robot in range(0, 4):
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_state = try_location_p2(grids,
                                            robot,
                                            (state[2][robot][0] + d[0],
                                             state[2][robot][1] + d[1]),
                                            state)

                if new_state is not None:
                    if len(new_state[1]) == key_count:
                        return new_state[0]
                    queue.append(new_state)
    return -1

def run():
    '''Main'''
    with open("inputs/day18.txt") as f:
        (grid, start, key_count) = load_data(f)

    return (find_route(grid, start, key_count),
            find_route_part2(grid, start, key_count))

if __name__ == '__main__':
    print(run())
