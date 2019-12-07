#!/usr/bin/python3
'''Advent of Code 2019 Day 5 tests'''
import unittest
import os
import sys
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import intcode # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day five, although we actually test intcode rather than day05.py'''
    def test_day05part1(self) -> None:
        '''Part one tests'''
        self.assertEqual(intcode.runprg([3, 0, 4, 0, 99], [12345]), 12345)
        self.assertEqual(intcode.runprg([1002, 4, 3, 4, 33]), 1002)

    def test_day05part2(self) -> None:
        '''Part two tests'''
        self.assertEqual(intcode.runprg([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8]), 1)
        self.assertEqual(intcode.runprg([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [7]), 0)
        self.assertEqual(intcode.runprg([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [8]), 0)
        self.assertEqual(intcode.runprg([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [7]), 1)
        self.assertEqual(intcode.runprg([3, 3, 1108, -1, 8, 3, 4, 3, 99], [8]), 1)
        self.assertEqual(intcode.runprg([3, 3, 1108, -1, 8, 3, 4, 3, 99], [7]), 0)
        self.assertEqual(intcode.runprg([3, 3, 1107, -1, 8, 3, 4, 3, 99], [8]), 0)
        self.assertEqual(intcode.runprg([3, 3, 1107, -1, 8, 3, 4, 3, 99], [7]), 1)

        prg = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(intcode.runprg(copy.copy(prg), [0]), 0)
        self.assertEqual(intcode.runprg(copy.copy(prg), [99]), 1)

        prg = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(intcode.runprg(copy.copy(prg), [0]), 0)
        self.assertEqual(intcode.runprg(copy.copy(prg), [99]), 1)

        prg = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006,
               20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20,
               1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4,
               20, 1105, 1, 46, 98, 99]
        self.assertEqual(intcode.runprg(copy.copy(prg), [7]), 999)
        self.assertEqual(intcode.runprg(copy.copy(prg), [8]), 1000)
        self.assertEqual(intcode.runprg(copy.copy(prg), [9]), 1001)
