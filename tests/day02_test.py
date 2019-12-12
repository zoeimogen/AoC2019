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
        '''Tests from day two, although all directly test intcode rather than day02.py'''
        pgm = intcode.Program('standard', [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        self.assertEqual(pgm.run(), [3500])
        pgm = intcode.Program('standard', [1, 0, 0, 0, 99])
        self.assertEqual(pgm.run(), [2])

        pgm = intcode.Program('standard', [2, 3, 0, 3, 99])
        pgm.run()
        self.assertEqual(pgm.state['pgm'][3], 6)

        pgm = intcode.Program('standard', [2, 4, 4, 5, 99, 0])
        pgm.run()
        self.assertEqual(pgm.state['pgm'][5], 9801)

        pgm = intcode.Program('standard', [1, 1, 1, 4, 99, 5, 6, 0, 99])
        self.assertEqual(pgm.run(), [30])
