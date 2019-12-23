#!/usr/bin/python3
'''Advent of Code 2019 Day 20 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day20 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day twenty'''
    def test_day20part1(self) -> None:
        '''Part one tests'''
        (grid, portals, start, target) = day20.load_data("tests/day20test01.txt")
        self.assertEqual(day20.find_route(grid, portals, start, target), 23)
        (grid, portals, start, target) = day20.load_data("tests/day20test02.txt")
        self.assertEqual(day20.find_route(grid, portals, start, target), 58)

    def test_day18part2(self) -> None:
        '''Part two tests'''
        (grid, portals, start, target) = day20.load_data("tests/day20test01.txt")
        self.assertEqual(day20.find_multilayer_route(grid, portals, start, target), 26)
        (grid, portals, start, target) = day20.load_data("tests/day20test02.txt")
        self.assertEqual(day20.find_multilayer_route(grid, portals, start, target), None)
        (grid, portals, start, target) = day20.load_data("tests/day20test03.txt")
        self.assertEqual(day20.find_multilayer_route(grid, portals, start, target), 396)
