#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 4 solution'''

from typing import Tuple

def checknumberpart1(n: int) -> int:
    '''Check number using the part one rules'''
    ns = f"{n}"
    if ns[0] != ns[1] and ns[1] != ns[2] and ns[2] != ns[3] and ns[3] != ns[4] and ns[4] != ns[5]:
        return False
    if (int(ns[0]) > int(ns[1]) or
            int(ns[1]) > int(ns[2]) or
            int(ns[2]) > int(ns[3]) or
            int(ns[3]) > int(ns[4]) or
            int(ns[4]) > int(ns[5])):
        return False
    return True

def checknumberpart2(n: int) -> int:
    '''Check number using the part two rules'''
    ns = f"{n}"
    if (not (ns[0] == ns[1] and ns[1] != ns[2])
            and not (ns[1] == ns[2] and ns[0] != ns[1] and ns[2] != ns[3])
            and not (ns[2] == ns[3] and ns[1] != ns[2] and ns[3] != ns[4])
            and not (ns[3] == ns[4] and ns[2] != ns[3] and ns[4] != ns[5])
            and not (ns[4] == ns[5] and ns[3] != ns[4])):
        return False
    if (int(ns[0]) > int(ns[1]) or
            int(ns[1]) > int(ns[2]) or
            int(ns[2]) > int(ns[3]) or
            int(ns[3]) > int(ns[4]) or
            int(ns[4]) > int(ns[5])):
        return False
    return True

def runpart1() -> int:
    '''Run part one'''
    count = 0
    for i in range(137683, 596254):
        if checknumberpart1(i):
            count += 1
    return count

def runpart2() -> int:
    '''Run part two'''
    count = 0
    for i in range(137683, 596254):
        if checknumberpart2(i):
            count += 1
    return count

def run() -> Tuple[int, int]:
    '''Main'''
    # Run the solution
    part1 = runpart1()
    part2 = runpart2()
    return (part1, part2)

if __name__ == '__main__':
    print(run())
