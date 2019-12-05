#!/usr/bin/python3
'''Advent of Code 2019 Day 3 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day04 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day04part1(self) -> None:
        '''Part One Tests'''
        self.assertEqual(day04.checknumberpart1(111111), True)
        self.assertEqual(day04.checknumberpart1(223450), False)
        self.assertEqual(day04.checknumberpart1(123789), False)

    def test_day04part2(self) -> None:
        '''Part Two Tests'''
        self.assertEqual(day04.checknumberpart2(112233), True)
        self.assertEqual(day04.checknumberpart2(123444), False)
        self.assertEqual(day04.checknumberpart2(111122), True)
