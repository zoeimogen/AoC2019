#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 22 partial solution'''

import re
import numpy

def dins(deck):
    '''Deal into new stack'''
    return list(reversed(deck))

def cut(deck, i):
    '''Cut the deck'''
    return list(deck[i:] + deck[:i])

def dwi(deck, i):
    '''Deal with increment'''
    deck_len = len(deck)
    new_deck = numpy.empty(deck_len, int)
    j = 0
    k = 0
    while True:
        new_deck[j] = deck[k]
        k += 1
        j = (j + i) % deck_len
        if j == 0:
            break
    return list(new_deck)

def shuffle(line, deck):
    '''Run a single shuffle command'''
    if re.match('deal into new stack', line):
        return dins(deck)

    if re.match(r'cut ([-\d]+)', line):
        i = int(re.match(r'cut ([-\d]+)', line).group(1))
        return cut(deck, i)

    if re.match(r'deal with increment (\d+)', line):
        i = int(re.match(r'deal with increment (\d+)', line).group(1))
        return dwi(deck, i)

    print(f'Unable to parse: {line}')
    return deck

def run():
    '''Main'''
    deck = list(range(0, 10007))

    with open("inputs/day22.txt") as f:
        for line in f:
            deck = shuffle(line, deck)
    part1 = deck.index(2019)

    return part1

if __name__ == '__main__':
    print(run())
