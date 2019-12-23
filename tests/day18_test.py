#!/usr/bin/python3
'''Advent of Code 2019 Day 18 tests'''
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from aoc2019 import day18 # pylint: disable=wrong-import-position

class TestUM(unittest.TestCase):
    '''Tests from day eighteen'''
    def test_day18part1(self) -> None:
        '''Part one tests'''
        (grid, start, key_count) = day18.load_data(['########################',
                                                    '#...............b.C.D.f#',
                                                    '#.######################',
                                                    '#.....@.a.B.c.d.A.e.F.g#',
                                                    '########################'])
        self.assertEqual(day18.find_route(grid, start, key_count), 132)

        (grid, start, key_count) = day18.load_data(['#################',
                                                    '#i.G..c...e..H.p#',
                                                    '########.########',
                                                    '#j.A..b...f..D.o#',
                                                    '########@########',
                                                    '#k.E..a...g..B.n#',
                                                    '########.########',
                                                    '#l.F..d...h..C.m#',
                                                    '#################'])
        self.assertEqual(day18.find_route(grid, start, key_count), 136)

        (grid, start, key_count) = day18.load_data(['########################',
                                                    '#@..............ac.GI.b#',
                                                    '###d#e#f################',
                                                    '###A#B#C################',
                                                    '###g#h#i################',
                                                    '########################'])
        self.assertEqual(day18.find_route(grid, start, key_count), 81)

    def test_day18part2(self) -> None:
        '''Part two tests'''
        (grid, start, key_count) = day18.load_data(['###############',
                                                    '#d.ABC.#.....a#',
                                                    '######...######',
                                                    '######.@.######',
                                                    '######...######',
                                                    '#b.....#.....c#',
                                                    '###############'])
        self.assertEqual(day18.find_route_part2(grid, start, key_count), 24)

        (grid, start, key_count) = day18.load_data(['#############',
                                                    '#DcBa.#.GhKl#',
                                                    '#.###...#I###',
                                                    '#e#d#.@.#j#k#',
                                                    '###C#...###J#',
                                                    '#fEbA.#.FgHi#',
                                                    '#############'])
        self.assertEqual(day18.find_route_part2(grid, start, key_count), 32)

        (grid, start, key_count) = day18.load_data(['#############',
                                                    '#g#f.D#..h#l#',
                                                    '#F###e#E###.#',
                                                    '#dCba...BcIJ#',
                                                    '#####.@.#####',
                                                    '#nK.L...G...#',
                                                    '#M###N#H###.#',
                                                    '#o#m..#i#jk.#',
                                                    '#############'])
        # self.assertEqual(day18.find_route_part2(grid, start, key_count), 72)
