#!/usr/bin/python3
'''Advent of Code 2019 Day 1 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day01 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day01part1(self) -> None:
        '''Test part 1'''
        self.assertEqual(day01.runpart1([12]), 2)
        self.assertEqual(day01.runpart1([14]), 2)
        self.assertEqual(day01.runpart1([1969]), 654)
        self.assertEqual(day01.runpart1([100756]), 33583)

    def test_day01part2(self) -> None:
        '''Test part 2'''
        self.assertEqual(day01.runpart2([14]), 2)
        self.assertEqual(day01.runpart2([1969]), 966)
        self.assertEqual(day01.runpart2([100756]), 50346)
