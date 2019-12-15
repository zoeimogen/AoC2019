#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 14 solution'''

from collections import defaultdict
from typing import Dict, List, Tuple
import math

Output = Tuple[int, str]
Inputs = List[Tuple[int, str]]
Reaction = Tuple[Inputs, Output]
Reactions = List[Reaction]

def read_reactions(inp: str) -> Reactions:
    '''Read reactions from a string'''
    reactions: Reactions = []
    for line in inp.splitlines():
        s = line.split(' => ')
        if len(s) == 2:
            inputs = [inp.split(' ') for inp in s[0].split(', ')]
            out = s[1].split(' ')
            r: Reaction = ([(int(i[0]), i[1]) for i in inputs],
                           (int(out[0]), out[1]))
            reactions.append(r)
    return reactions

def find_answer(reactions: Reactions, fuel):
    '''Solve part one'''
    need: Dict[str, int] = defaultdict(int)
    need['FUEL'] = fuel

    while True:
        # Find one thing in our needs list other than ore, and find the reaction that
        # generates it. This won't work if more than one reaction can generate a need,
        # but that's not the case with any input reaction sets we have.
        needs = [n for n in need if n != 'ORE' and need[n] > 0]
        if not needs:
            # We only need ore, so we're done.
            break

        this_need = needs[0]
        n = need[this_need]

        # Supply is the required reaction.
        supply = [r for r in reactions if r[1][1] == this_need][0]
        # Using is how many times the reacion needs to run.
        using = math.ceil(n / supply[1][0])
        # Generating is the resulting amount of output material, which may include some surplus
        generating = supply[1][0] * using
        # Add correct quantities of our inputs from the reaction to the needs
        for s in supply[0]:
            need[s[1]] += s[0] * using
        # Remove the generated output from the needs list. Negative needs means we have a surplus.
        need[this_need] -= generating
    return need['ORE']

def runpart2(reactions: Reactions, target: int):
    '''Solve part 2'''

    # Not a very elegant or efficient algorithm, but it works.
    increment = 1000000
    current = increment

    # Go up in jumps of increment, until the ore required exceeds the target. Then
    # divide the increment by ten and repeat from the previous step.
    while increment >= 1:
        answer = find_answer(reactions, current)
        if answer < target:
            current += increment
        else:
            current -= increment
            increment = increment // 10

    return current

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day14.txt") as f:
        reactions = read_reactions(f.read())

    # Run the solution
    return(find_answer(reactions, 1), runpart2(reactions, 1000000000000))

if __name__ == '__main__':
    print(run())
