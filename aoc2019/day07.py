#!/usr/bin/env python3
# pylint: disable=invalid-name, dangerous-default-value
'''Advent of Code 2019 Day 7 solution
   https://adventofcode.com/2019/day/7'''

import copy
from typing import List, Tuple, Callable
from aoc2019.intcode import runprg, runprg_iterate

Program = List[int]
Sequencer = Callable[[List[int], Program], int]

def check_sequence(seq: List[int], prg: Program) -> int:
    '''Sequencer for part 1 - run all five amplifier programs for a given sequence

    Args:
        seq: The sequence of amplifier phase settings for this run
        prg: The program to run. (Immutable, we use copy.copy on it)

    Returns:
        An int containing the final amplifier output'''

    i = 0

    # For every amplifier, run it and feed the input (i) from the previous step in to it
    for a in range(0, 5):
        i = runprg(copy.copy(prg), [seq[a], i])

    return i

def check_loopback_sequence(seq: List[int], prg: Program) -> int:
    '''Sequence for part 2 - run amplifier programs for a given sequence

    Args:
        seq: The sequence of amplifier phase settings for this run
        prg: The program to run. (Immutable, we use copy.copy on it)

    Returns:
        An int containing the final amplifier output'''

    # Make a copy of all five programs, because we need to store state
    prgs: List[Program] = []
    for _ in range(0, 5):
        prgs.append(copy.copy(prg))

    # Keep track of instruction pointers (IP)
    ips = [0, 0, 0, 0, 0]

    i = 0

    # Initial run through including phase input
    for a in range(0, 5):
        # Note that prgs is pass-by-reference, but we need to explicitly store the new IP.
        (ips[a], new_i) = runprg_iterate(prgs[a], [seq[a], i], ips[a])
        if new_i is None:
            # This should never happen unless we have bad code, but it keeps the type checker happy.
            raise Exception()
        i = new_i

    # Loopback runs. Keep running until runprg_iterate returns None, indicating it exited.
    while True:
        for a in range(0, 5):
            (ips[a], new_i) = runprg_iterate(prgs[a], [i], ips[a])
            if new_i is None:
                return i
            i = new_i

def iterate_sequences(rem: List[int],
                      prg: Program,
                      sequencer: Sequencer,
                      seq: List[int] = []) -> int:
    '''Outer loop - depth-first search of every possible phase sequence on an program

    Args:
        rem: List of phase values to be tried.
        prg: The program to run.
        sequencer: The sequencer to use for this run. (Loopback or non-loopback)
        seq: The sequence of amplifier phase settings for this run already set. Used for recursion.

    Returns:
        An int containing the maximum amplifier output'''

    # Have we already reached the bottom of the search tree? If so, run the sequence.
    if len(rem) == 1:
        return sequencer(seq + rem, prg)

    max_power = 0
    # For each remaining phase setting...
    for (a, r) in enumerate(rem):
        # Search one level deeper using that phase setting, and record the maximum power found
        max_power = max(max_power,
                        iterate_sequences(rem[:a] + rem[a+1:], prg, sequencer, seq + [r]))

    return max_power

def run() -> Tuple[int, int]:
    '''Main'''

    # Read program and put into data
    data: Program = []
    with open("inputs/day07.txt") as f:
        data = list(map(int, f.readline().split(',')))

    # Run the solution
    part1 = iterate_sequences(list(range(0, 5)), data, check_sequence)
    part2 = iterate_sequences(list(range(5, 10)), data, check_loopback_sequence)
    return(part1, part2)

if __name__ == '__main__':
    print(run())
