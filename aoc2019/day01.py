#!/usr/bin/env python3
'''Advent of Code 2019 Day 1 solution'''
from typing import List, Tuple
import math

def runpart1(data: List[int]) -> int:
    '''Run part one'''
    def fuel(mass: int) -> int:
        return math.floor(mass / 3) - 2

    return sum([fuel(m) for m in data])

def runpart2(data: List[int]) -> int:
    '''Run part two'''
    def fuel(mass: int) -> int:
        this_fuel = math.floor(mass / 3) - 2
        if this_fuel <= 0:
            return 0
        return this_fuel+fuel(this_fuel)

    return sum([fuel(m) for m in data])

def run() -> Tuple[int, int]:
    '''Main'''

    # Read input file and put into data
    data = []
    with open("inputs/day01.txt") as file:
        for line in file:
            try:
                data.append(int(line))
            except ValueError:
                pass

    # Run the solution
    part1 = runpart1(data)
    part2 = runpart2(data)
    return (part1, part2)

if __name__ == '__main__':
    print(run())
