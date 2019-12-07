#!/usr/bin/python3
'''Advent of Code 2019 Day 7 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day07 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day seven'''
    def test_day07part1(self) -> None:
        '''Part one tests'''
        test1 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        test2 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
        test3 = ('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,'
                 '1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0')

        self.assertEqual(day07.iterate_sequences(list(range(0, 5)),
                                                 list(map(int, test1.split(','))),
                                                 day07.check_sequence),
                         43210)

        self.assertEqual(day07.iterate_sequences(list(range(0, 5)),
                                                 list(map(int, test2.split(','))),
                                                 day07.check_sequence),
                         54321)

        self.assertEqual(day07.iterate_sequences(list(range(0, 5)),
                                                 list(map(int, test3.split(','))),
                                                 day07.check_sequence),
                         65210)

    def test_day07part2(self) -> None:
        '''Part two tests'''
        test1 = ('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,'
                 '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5')
        test2 = ('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,'
                 '-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,'
                 '53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10')

        self.assertEqual(day07.iterate_sequences(list(range(5, 10)),
                                                 list(map(int, test1.split(','))),
                                                 day07.check_loopback_sequence),
                         139629729)

        self.assertEqual(day07.iterate_sequences(list(range(5, 10)),
                                                 list(map(int, test2.split(','))),
                                                 day07.check_loopback_sequence),
                         18216)
