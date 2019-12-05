#!/usr/bin/python3
'''Advent of Code 2019 Day 2 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import intcode # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Unit Tests'''
    def test_day02(self) -> None:
        '''Tests from day two, although we actually test intcode rather than day02.py'''
        self.assertEqual(intcode.runprg([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]), 3500)
        self.assertEqual(intcode.runprg([1, 0, 0, 0, 99]), 2)

        prg = [2, 3, 0, 3, 99]
        intcode.runprg(prg)
        self.assertEqual(prg[3], 6)

        prg = [2, 4, 4, 5, 99, 0]
        intcode.runprg(prg)
        self.assertEqual(prg[5], 9801)

        self.assertEqual(intcode.runprg([1, 1, 1, 4, 99, 5, 6, 0, 99]), 30)
