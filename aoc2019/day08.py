#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Day 8 solution
   https://adventofcode.com/2019/day/8'''

from typing import List, Tuple

Size = Tuple[int, int]
Image = List[List[int]]

def read_image(size: Size, data: str) -> Image:
    '''Convert a text string into a layered image'''
    data = data.rstrip()
    image: Image = []
    while data != '':
        layer = data[:size[0] * size[1]]
        image.append(list(map(int, layer)))
        data = data[size[0] * size[1]:]

    return image

def zero_layer(size: Size, image: Image) -> int:
    '''Part 1: Find the layer with most zeros and return ones times twos'''
    minimum_zeros = (0, size[0] * size[1])
    for (i, layer) in enumerate(image):
        zeros = len([pixel for pixel in layer if pixel == 0])
        if zeros < minimum_zeros[1]:
            minimum_zeros = (i, zeros)

    ones = len([a for a in image[minimum_zeros[0]] if a == 1])
    twos = len([a for a in image[minimum_zeros[0]] if a == 2])
    return ones * twos

def flatten_image(size: Size, image: Image) -> str:
    '''Part 2: Flatten an image into a string'''
    flat_image = [2 for _ in range(0, size[0] * size[1])]
    for layer in image:
        for (i, pixel) in enumerate(layer):
            if flat_image[i] == 2:
                flat_image[i] = pixel

    output = ''
    for i in range(0, size[0]):
        for j in range(0, size[1]):
            if flat_image[i*size[1] + j] == 1:
                output += '#'
            else:
                output += ' '
        output += "\n"

    return output

def run() -> Tuple[int, str]:
    '''Main'''
    SIZE = (6, 25)

    with open("inputs/day08.txt") as f:
        data = f.readline()

    image = read_image(SIZE, data)

    # Run the solution
    part1 = zero_layer(SIZE, image)
    part2 = flatten_image(SIZE, image)
    return(part1, part2)

if __name__ == '__main__':
    print(run())
