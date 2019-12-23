#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 23 solution'''

import copy
from typing import Tuple
from aoc2019 import intcode

def run_network(pgm):
    '''Run the intcode network'''
    computers = []
    for c in range(0, 50):
        computers.append(intcode.Program('network', copy.copy(pgm), [c]))

    while True:
        for c in range(0, 50):
            if computers[c].state['ptr'] != -1:
                computers[c].intcode()
            if len(computers[c].state['outputs']) >= 3:
                dst = computers[c].state['outputs'].pop(0)
                x = computers[c].state['outputs'].pop(0)
                y = computers[c].state['outputs'].pop(0)
                if dst == 255:
                    return y
                computers[dst].state['inputs'].append(x)
                computers[dst].state['inputs'].append(y)

def run_network_p2(pgm):
    '''Run the intcode network with NAT'''
    computers = []
    for c in range(0, 50):
        computers.append(intcode.Program('network', copy.copy(pgm), [c]))

    nat = (0, 0)
    while True:
        for c in range(0, 50):
            if computers[c].state['ptr'] != -1:
                computers[c].intcode()
            if len(computers[c].state['outputs']) >= 3:
                dst = computers[c].state['outputs'].pop(0)
                x = computers[c].state['outputs'].pop(0)
                y = computers[c].state['outputs'].pop(0)
                if dst == 255:
                    if y == nat[1]:
                        return y
                    nat = (x, y)
                else:
                    computers[dst].state['inputs'].append(x)
                    computers[dst].state['inputs'].append(y)
            if len([i for i in computers if i.state['idle'] < 2]) == 0:
                computers[0].state['idle'] = 0
                computers[0].state['inputs'].append(nat[0])
                computers[0].state['inputs'].append(nat[1])

def run() -> Tuple[int, int]:
    '''Main'''
    # Read program and put into data
    with open("inputs/day23.txt") as f:
        data = list(map(int, f.readline().split(',')))

    part1 = run_network(data)
    part2 = run_network_p2(data)
    return(part1, part2)

if __name__ == '__main__':
    print(run())
