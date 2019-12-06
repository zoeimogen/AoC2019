#!/usr/bin/python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 6 tests'''

import unittest
import os
import sys
from typing import List, Dict
from collections import defaultdict
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day06 # pylint: disable=wrong-import-position

Orbits = Dict[str, List[str]]

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day06part1(self) -> None:
        '''Part One Tests'''
        orbits: Orbits = defaultdict(list)
        testdata = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
        for line in testdata.split('\n'):
            (a, b) = line.rstrip().split(')')
            orbits[a].append(b)
        self.assertEqual(day06.orbit_count('COM', orbits, 0), 42)

    def test_day06part2(self) -> None:
        '''Part Two Tests'''
        orbits: Orbits = defaultdict(list)
        testdata = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN"
        for line in testdata.split('\n'):
            (a, b) = line.rstrip().split(')')
            orbits[a].append(b)
        self.assertEqual(day06.runpart2(orbits), 4)
