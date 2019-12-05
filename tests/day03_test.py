#!/usr/bin/python3
'''Advent of Code 2019 Day 3 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day03 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day03part1(self) -> None:
        '''Part One Tests'''
        self.assertEqual(day03.single_run('R8,U5,L5,D3'.split(','),
                                          'U7,R6,D4,L4'.split(','),
                                          True), 6)
        self.assertEqual(day03.single_run('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                                          'U62,R66,U55,R34,D71,R55,D58,R83'.split(','),
                                          True), 159)
        self.assertEqual(day03.single_run('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                                          'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','),
                                          True), 135)

    def test_day03part2(self) -> None:
        '''Part Two Tests'''
        self.assertEqual(day03.single_run('R8,U5,L5,D3'.split(','),
                                          'U7,R6,D4,L4'.split(','),
                                          False), 30)
        self.assertEqual(day03.single_run('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                                          'U62,R66,U55,R34,D71,R55,D58,R83'.split(','),
                                          False), 610)
        self.assertEqual(day03.single_run('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                                          'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(','),
                                          False), 410)
