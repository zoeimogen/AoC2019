#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 2 solution'''

import copy
from typing import List, Tuple

Program = List[int]

def bad(program: Program, ptr: int) -> int:
    '''Invalid Opcode'''
    raise Exception

def add(program: Program, ptr: int) -> int:
    '''Add'''
    a = program[program[ptr+1]]
    b = program[program[ptr+2]]
    c = a + b
    program[program[ptr+3]] = c
    return ptr + 4

def mul(program: Program, ptr: int) -> int:
    '''Multiply'''
    a = program[program[ptr+1]]
    b = program[program[ptr+2]]
    c = a * b
    program[program[ptr+3]] = c
    return ptr + 4

def intcode(program: Program, ptr: int) -> int:
    '''Run a single instruction'''
    opcode = [bad, add, mul]
    if program[ptr] == 99:
        return -1
    return opcode[program[ptr]](program, ptr)

def runprg(program: Program) -> int:
    '''Run a program'''
    p = 0
    while True:
        p = intcode(program, p)
        if p == -1:
            break
    return program[0]

def runpart1(program: Program, noun: int, verb: int) -> int:
    '''Run part one'''
    prg = copy.copy(program)
    prg[1] = noun
    prg[2] = verb
    return runprg(prg)

def runpart2(program: Program) -> int:
    '''Run part two'''
    def run2(program: Program, noun: int, verb: int) -> int:
        prg = copy.copy(program)
        prg[1] = noun
        prg[2] = verb
        runprg(prg)
        return prg[0]

    for x in range(0, 100):
        for y in range(0, 100):
            if run2(program, x, y) == 19690720:
                return x*100 + y

    return 0 # Failed to find a solution

def run() -> Tuple[int, int]:
    '''Main'''

    # Read program and put into data
    with open("../inputs/day02.txt") as f:
        data = list(map(int, f.readline().split(',')))

    # Run the solution
    part1 = runpart1(data, 12, 2)
    part2 = runpart2(data)
    return (part1, part2)

if __name__ == '__main__':
    print(run())
