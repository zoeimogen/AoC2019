#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 6 solution'''

from collections import defaultdict
from typing import List, Tuple, Dict
Orbits = Dict[str, List[str]]

def orbit_count(body: str, orbits: Orbits, depth: int) -> int:
    '''Solution to part 1 - count the depth of the orbits'''
    count = depth
    for b in orbits[body]:
        count += orbit_count(b, orbits, depth + 1)
    return count

def find_orbit_path(body: str, orbits: Orbits, target: str, path: List[str]) -> List[str]:
    '''Find the path to a given target'''
    for b in orbits[body]:
        if b == target:
            return [b]
        p = find_orbit_path(b, orbits, target, path + [b])
        if p != []:
            return [b] + p
    return []

def runpart2(orbits: Orbits) -> int:
    '''Solve part 2'''
    yourorbit = find_orbit_path('COM', orbits, 'YOU', [])
    santaorbit = find_orbit_path('COM', orbits, 'SAN', [])
    while yourorbit[0] == santaorbit[0]:
        yourorbit.pop(0)
        santaorbit.pop(0)
    return len(yourorbit) + len(santaorbit) - 2

def run() -> Tuple[int, int]:
    '''Main'''
    orbits: Orbits = defaultdict(list)
    with open("inputs/day06.txt") as f:
        for line in f:
            (a, b) = line.rstrip().split(')')
            orbits[a].append(b)

    part1 = orbit_count('COM', orbits, 0)
    part2 = runpart2(orbits)

    return(part1, part2)
if __name__ == '__main__':
    print(run())
