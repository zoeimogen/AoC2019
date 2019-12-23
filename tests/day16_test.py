#!/usr/bin/python3
'''Advent of Code 2019 Day 16 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day16 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day fourteen'''
    def test_day16part1(self) -> None:
        '''Part one tests'''
        self.assertEqual(day16.cycle([int(i) for i in '12345678'], 3), 3415518)
        self.assertEqual(day16.cycle([int(i)
                                      for i in '80871224585914546619083218645595'], 100), 24176176)
        self.assertEqual(day16.cycle([int(i)
                                      for i in '19617804207202209144916044189917'], 100), 73745418)
        self.assertEqual(day16.cycle([int(i)
                                      for i in '69317163492948606335995924319873'], 100), 52432133)
