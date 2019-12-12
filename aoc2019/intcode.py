#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Intcode interpreter'''

from typing import List #, Tuple, Union, Dict, Any
import copy
import numpy

Pgm = List[int]

class Program:
    '''An intcode program execution environment'''
    def __init__(self, ptype, prg, inputs=None):
        self.state = {'type': ptype,
                      'pgm': copy.copy(prg),
                      'ptr': 0,
                      'rel': 0,
                      'outputs': []}

        if inputs:
            self.state['inputs'] = inputs

        if ptype == 'robot':
            self.state['direction'] = 0
            self.state['location'] = [0, 0]
            self.state['grid'] = numpy.zeros((100, 100), int)
            self.state['output_state'] = 0

    @staticmethod
    def _bad(_1, _2, _3)  -> None:
        '''Bad instruction'''
        raise Exception()

    def _add(self, args: List[int], opts: List[int])  -> None:
        '''Add'''
        self.state['pgm'][opts[0]] = args[0] + args[1]
        self.state['ptr'] += 4

    def _mul(self, args: List[int], opts: List[int])  -> None:
        '''Multiply'''
        self.state['pgm'][opts[0]] = args[0] * args[1]
        self.state['ptr'] += 4

    def _inp(self, _1, opts: List[int])  -> None:
        '''Input'''
        if self.state['type'] == 'robot':
            x = self.state['location'][0] + 50
            y = self.state['location'][1] + 50
            panel = self.state['grid'][x][y]
            if panel > 0:
                panel -= 1
            self.state['pgm'][opts[0]] = panel
        else:
            self.state['pgm'][opts[0]] = self.state['inputs'].pop(0)
        self.state['ptr'] += 2

    def _out_robot(self, arg: int) -> None:
        if self.state['output_state'] == 0:
            # Paint
            x = self.state['location'][0] + 50
            y = self.state['location'][1] + 50
            self.state['grid'][x][y] = arg + 1
            self.state['output_state'] = 1
        else:
            # Turn and move
            if arg == 0:
                self.state['direction'] -= 1
                if self.state['direction'] < 0:
                    self.state['direction'] = 3
            else:
                self.state['direction'] += 1
                if self.state['direction'] > 3:
                    self.state['direction'] = 0

            if self.state['direction'] == 0:
                self.state['location'][0] -= 1
            elif self.state['direction'] == 1:
                self.state['location'][1] += 1
            elif self.state['direction'] == 2:
                self.state['location'][0] += 1
            else:
                self.state['location'][1] -= 1

            self.state['output_state'] = 0

    def _out(self, args: List[int], _)  -> None:
        '''Output'''
        if self.state['type'] == 'robot':
            self._out_robot(args[0])
        else:
            self.state['outputs'].append(args[0])
        self.state['ptr'] += 2

    def _jit(self, args: List[int], _)  -> None:
        '''Jump if true'''
        if args[0]:
            self.state['ptr'] = args[1]
        else:
            self.state['ptr'] += 3

    def _jif(self, args: List[int], _)  -> None:
        '''Jump if false'''
        if not args[0]:
            self.state['ptr'] = args[1]
        else:
            self.state['ptr'] += 3

    def _lt(self, args: List[int], opts: List[int])  -> None:
        '''Less than'''
        self.state['pgm'][opts[0]] = int(args[0] < args[1])
        self.state['ptr'] += 4

    def _eq(self, args: List[int], opts: List[int]) -> None:
        '''Equals'''
        self.state['pgm'][opts[0]] = int(args[0] == args[1])
        self.state['ptr'] += 4

    def _rba(self, args: List[int], _) -> None:
        '''Equals'''
        self.state['rel'] += args[0]
        self.state['ptr'] += 2

    def intcode(self) -> None:
        '''Run a single instruction'''
        OPCODE = [(self._bad, 0, 0),
                  (self._add, 2, 1), # 1
                  (self._mul, 2, 1), # 2
                  (self._inp, 0, 1), # 3
                  (self._out, 1, 0), # 4
                  (self._jit, 2, 0), # 5
                  (self._jif, 2, 0), # 6
                  (self._lt, 2, 1),  # 7
                  (self._eq, 2, 1),  # 8
                  (self._rba, 1, 0)]

        if self.state['pgm'][self.state['ptr']] == 99:
            self.state['ptr'] = -1
            return

        try:
            code = self.state['pgm'][self.state['ptr']]
        except IndexError:
            print(f"Illegal Pointer {self.state['ptr']}")
            self.state['ptr'] = -1
            return

        try:
            instruction = OPCODE[code % 100]
        except IndexError:
            print(f"Illegal instruction {code} at {self.state['ptr']}")
            self.state['ptr'] = -1
            return

        parameters = code // 100
        argcount = instruction[1]
        args = []
        opts = []
        i = 1
        while argcount:
            if parameters % 10 == 2:
                # Relative load
                args.append(self.state['pgm'][self.state['pgm'][self.state['ptr']+i] +
                                              self.state['rel']])
            elif parameters % 10 == 1:
                # Immediate load
                args.append(self.state['pgm'][self.state['ptr']+i])
            else:
                # Position load
                try:
                    args.append(self.state['pgm'][self.state['pgm'][self.state['ptr']+i]])
                except IndexError:
                    args.append(0)
            parameters = parameters // 10
            argcount -= 1
            i += 1

        optcount = instruction[2]
        while optcount:
            if parameters % 10 == 2:
                # Relative load
                opts.append(self.state['pgm'][self.state['ptr']+i] + self.state['rel'])
            else:
                opts.append(self.state['pgm'][self.state['ptr']+i])
            if opts[-1] >= len(self.state['pgm']):
                self.state['pgm'].extend(numpy.zeros(1 + opts[-1] - len(self.state['pgm'])))
            parameters = parameters // 10
            optcount -= 1
            i += 1

        instruction[0](args, opts)

    def run(self) -> List[int]:
        '''Run a program'''
        while self.state['ptr'] != -1:
            # print(self.state['ptr'])
            self.intcode()
            if self.state['type'] == 'iterate' and self.state['outputs']:
                return [self.state['outputs'].pop()]

        if self.state['outputs']:
            return self.state['outputs']

        return [self.state['pgm'][0]]

    # def runprg_robot(program: Program) -> List[List[int]]:
    #     '''Run a program'''
    #     p = 0
    #     state = {'type': 'robot',
    #              'rel': 0,
    #              'outputs': [],
    #              'direction': 0,
    #              'location': [0, 0],
    #              'grid': numpy.zeros((100, 100), int),
    #              'output_state': 0}
    #     state['grid'][50][50] = 2
    #     program.extend((map(int, numpy.zeros(1000))))
    #     while True:
    #         p = intcode(program, p, [], state)
    #         if p == -1:
    #             break

    #     return state['grid']
