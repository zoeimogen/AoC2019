#!/usr/bin/python3
'''Advent of Code 2019 Day 5 tests'''
import unittest
import os
import sys
import numpy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import intcode # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day nine, although we actually test intcode rather than day09.py'''
    def test_day09part1(self) -> None:
        '''Part one tests'''
        prg = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        prg.extend((map(int, numpy.zeros(100))))
        intcode.runprg(prg)
        self.assertEqual(prg[-16:], prg[:16])

        prg = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        prg.extend((map(int, numpy.zeros(100))))
        self.assertEqual(len(f"{intcode.runprg(prg)}"), 16)

        prg = [104, 1125899906842624, 99]
        self.assertEqual(intcode.runprg(prg), prg[1])
