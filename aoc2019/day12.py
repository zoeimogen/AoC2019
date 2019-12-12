#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 11 solution'''

from typing import Tuple, List
import copy
import math
import re

def step(moons: List[int]) -> None:
    '''Simulate one step of the universe'''
    for a in range(0, 4):
        for b in range(a+1, 4):
            for axis in range(0, 3):
                if moons[a*6+axis] < moons[b*6+axis]:
                    moons[a*6+axis+3] += 1
                    moons[b*6+axis+3] -= 1
                elif moons[a*6+axis] > moons[b*6+axis]:
                    moons[a*6+axis+3] -= 1
                    moons[b*6+axis+3] += 1
    for moon in range(0, 4):
        for axis in range(0, 3):
            moons[moon*6+axis] += moons[moon*6+axis+3]

def energy(moons: List[int]) -> int:
    '''Calculate the energy of the system'''
    e = 0
    for moon in range(0, 4):
        e += (sum([abs(p) for p in moons[moon*6:moon*6+3]]) *
              sum([abs(v) for v in moons[moon*6+3:moon*6+6]]))
    return e

def lowest_common_multiple(x: int, y: int) -> int:
    '''Lowest common multiple of a pair of numbers'''
    return x * y // math.gcd(x, y)

def find_cycle(moons: List[int]) -> int:
    '''Find a cycle in the system.'''

    # Each axis is independent, so we can find each cycle individually.
    solved = [0, 0, 0]

    target_state = {}
    for axis in range(0, 3):
        thisaxis = [moons[axis], moons[axis+6], moons[axis+12],
                    moons[axis+3], moons[axis+9], moons[axis+15]]
        target_state[axis] = thisaxis

    loop_counter = 1
    while [s for s in solved if not s]:
        step(moons)

        for axis in range(0, 3):
            if not solved[axis]:
                thisaxis = [moons[axis], moons[axis+6], moons[axis+12],
                            moons[axis+3], moons[axis+9], moons[axis+15]]
                if thisaxis == target_state[axis]:
                    solved[axis] = loop_counter
        loop_counter += 1

    # The overall cycle is the lowest common multiple of the three axes.
    return lowest_common_multiple(lowest_common_multiple(solved[0], solved[1]), solved[2])

def do_part1(moons: List[int], cycles: int) -> int:
    '''Solve part 1'''
    m = copy.copy(moons)

    for _ in range(0, cycles):
        step(m)

    return energy(m)

def load_moons(data: str) -> List[int]:
    '''Load moon datafrom file or string'''
    moons = []
    scan = re.compile(r'<x=([-\d]*), y=([-\d]*), z=([-\d]*)>')

    for line in data.splitlines():
        m = scan.match(line)
        if m:
            moons.extend([int(m.group(1)),
                          int(m.group(2)),
                          int(m.group(3)), 0, 0, 0])

    return moons

def run() -> Tuple[int, int]:
    '''Main'''
    with open("inputs/day12.txt") as f:
        moons = load_moons(f.read())

    part1 = do_part1(moons, 10000)
    part2 = find_cycle(moons)

    return (part1, part2)

if __name__ == '__main__':
    print(run())
