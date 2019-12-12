#!/usr/bin/env python3
'''Advent of Code 2019 run all solutions'''

from timeit import timeit

for i in range(1, 13):
    if i in [8, 11]:
        print(' in %.2fs' % (timeit(f'print("Day {i}: %d\\n%s" % aoc2019.day{i:02}.run(), end="")',
                                    'import aoc2019.day%02d' % (i),
                                    number=1)))
    else:
        print(' in %.2fs' % (timeit('print("Day %d: ", aoc2019.day%02d.run(), end="")' % (i, i),
                                    'import aoc2019.day%02d' % (i),
                                    number=1)))
