#!/usr/bin/env python3
# pylint: disable=invalid-name, dangerous-default-value
'''Advent of Code 2019 Intcode interpreter'''

from typing import List, Tuple, Union

Program = List[int]

def _bad(_: Program, __: int, ___: List[int], ____: List[int], _____: List[int]) -> int:
    '''Bad instruction'''
    raise Exception()

def _add(program: Program, ptr: int, args: List[int], opts: List[int], _: List[int]) -> int:
    '''Add'''
    program[opts[0]] = args[0] + args[1]
    return ptr + 4

def _mul(program: Program, ptr: int, args: List[int], opts: List[int], _: List[int]) -> int:
    '''Multiply'''
    program[opts[0]] = args[0] * args[1]
    return ptr + 4

def _inp(program: Program, ptr: int, _: List[int], opts: List[int], i: List[int]) -> int:
    '''Input'''
    # print(f"Setting {opts[0]} to {i}")
    program[opts[0]] = i.pop(0)
    return ptr + 2

def _out(program: Program, ptr: int, args: List[int], __: List[int], ___: List[int]) -> int:
    '''Output'''
    program.append(args[0])
    return ptr + 2

def _jit(_: Program, ptr: int, args: List[int], __: List[int], ___: List[int]) -> int:
    '''Jump if true'''
    if args[0]:
        return args[1]
    return ptr + 3

def _jif(_: Program, ptr: int, args: List[int], __: List[int], ___: List[int]) -> int:
    '''Jump if false'''
    if not args[0]:
        return args[1]
    return ptr + 3

def _lt(program: Program, ptr: int, args: List[int], opts: List[int], _: List[int]) -> int:
    '''Less than'''
    program[opts[0]] = int(args[0] < args[1])
    return ptr + 4

def _eq(program: Program, ptr: int, args: List[int], opts: List[int], _: List[int]) -> int:
    '''Equals'''
    program[opts[0]] = int(args[0] == args[1])
    return ptr + 4

def intcode(program: Program, ptr: int, indata: List[int]) -> int:
    '''Run a single instruction'''
    opcode = [(_bad, 0, 0),
              (_add, 2, 1), # 1
              (_mul, 2, 1), # 2
              (_inp, 0, 1), # 3
              (_out, 1, 0), # 4
              (_jit, 2, 0), # 5
              (_jif, 2, 0), # 6
              (_lt, 2, 1),  # 7
              (_eq, 2, 1)]  # 8

    if program[ptr] == 99:
        return -1

    try:
        code = program[ptr]
    except IndexError:
        print(f"Illegal Pointer {ptr}")
        return -1

    try:
        instruction = opcode[code % 100]
    except IndexError:
        print(f"Illegal instruction {code} at {ptr}")
        return -1

    parameters = code // 100
    argcount = instruction[1]
    args = []
    opts = []
    i = 1
    while argcount:
        if parameters % 10:
            # Immediate load
            args.append(program[ptr+i])
        else:
            # Position load
            args.append(program[program[ptr+i]])
        parameters = parameters // 10
        argcount -= 1
        i += 1

    optcount = instruction[2]
    while optcount:
        opts.append(program[ptr+i])
        optcount -= 1
        i += 1

    return instruction[0](program, ptr, args, opts, indata)

def runprg(program: Program, indata: List[int] = [0]) -> int:
    '''Run a program'''
    p = 0
    initial_length = len(program)
    while True:
        p = intcode(program, p, indata)
        if p == -1:
            break

    # If we output anything, it's appended to the end of the program - return it.
    # If not, just return the value of the first program entry.
    if len(program) > initial_length:
        return program[-1]
    return program[0]

def runprg_iterate(program: Program,
                   indata: List[int] = [0],
                   p: int = 0) -> Tuple[int, Union[int, None]]:
    '''Run a program that iterates'''
    initial_length = len(program)
    while True:
        p = intcode(program, p, indata)
        if len(program) > initial_length:
            return (p, program[-1])
        if p == -1:
            return (p, None)
