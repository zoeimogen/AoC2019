#!/usr/bin/python3
'''Advent of Code 2019 Day 12 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day12 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day twelve'''

    test1 = '''
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

    test2 = '''
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''

    def test_day11part1(self) -> None:
        '''Part one tests'''
        moons = day12.load_moons(self.test1)
        self.assertEqual(day12.do_part1(moons, 10), 179)
        moons = day12.load_moons(self.test2)
        self.assertEqual(day12.do_part1(moons, 100), 1940)

    def test_day10part2(self) -> None:
        '''Part two test'''
        moons = day12.load_moons(self.test1)
        self.assertEqual(day12.find_cycle(moons), 2772)
        moons = day12.load_moons(self.test2)
        self.assertEqual(day12.find_cycle(moons), 4686774924)
