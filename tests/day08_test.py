#!/usr/bin/python3
'''Advent of Code 2019 Day 8 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day08 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day seven'''
    def test_day07part1(self) -> None:
        '''Part one tests'''
        image = day08.read_image((3, 2), '123456789012')
        self.assertEqual(day08.zero_layer((3, 2), image), 1)

    def test_day07part2(self) -> None:
        '''Part two test'''
        image = day08.read_image((2, 2), '0222112222120000')
        self.assertEqual(day08.flatten_image((2, 2), image), ' #\n# \n')
