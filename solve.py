#!/usr/bin/env python3
'''Advent of Code 2019 run all solutions'''

from timeit import timeit

for i in range(1, 7):
    print(' in %.2fs' % (timeit('print("Day %d: ", aoc2019.day%02d.run(), end="")' % (i, i),
                                'import aoc2019.day%02d' % (i),
                                number=1)))
