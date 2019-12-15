#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Advent of Code 2019 Intcode interpreter'''

import copy
import time
import numpy

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

        if ptype == 'arcade':
            self.state['location'] = [0, 0]
            self.state['grid'] = numpy.zeros((26, 40), int)
            self.state['output_state'] = 0
            self.state['score'] = 0
            self.state['ball'] = 0
            self.state['paddle'] = 0
            self.state['show_grid'] = False

    @staticmethod
    def _bad(_1, _2, _3):
        '''Bad instruction'''
        raise Exception()

    def _add(self, args, opts):
        '''Add'''
        self.state['pgm'][opts[0]] = args[0] + args[1]
        self.state['ptr'] += 4

    def _mul(self, args, opts):
        '''Multiply'''
        self.state['pgm'][opts[0]] = args[0] * args[1]
        self.state['ptr'] += 4

    def _inp(self, _1, opts):
        '''Input'''
        if self.state['type'] == 'robot':
            x = self.state['location'][0] + 50
            y = self.state['location'][1] + 50
            panel = self.state['grid'][x][y]
            if panel > 0:
                panel -= 1
            self.state['pgm'][opts[0]] = panel
        elif self.state['type'] == 'arcade':
            if self.state['paddle'] < self.state['ball']:
                self.state['pgm'][opts[0]] = 1
            elif self.state['paddle'] > self.state['ball']:
                self.state['pgm'][opts[0]] = -1
            else:
                self.state['pgm'][opts[0]] = 0
        else:
            self.state['pgm'][opts[0]] = self.state['inputs'].pop(0)
        self.state['ptr'] += 2

    def _out_robot(self, arg: int):
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

    def show_grid(self):
        '''Shows the grid, in case you want to watch the game'''
        print("\033[0;0H")
        for x in self.state['grid']:
            for y in x:
                if y == 1:
                    print('#', end='')
                elif y == 2:
                    print('*', end='')
                elif y == 3:
                    print('-', end='')
                elif y == 4:
                    print('o', end='')
                else:
                    print(' ', end='')
            print('')
        print(f"Score: {self.state['score']}")
        time.sleep(.02)

    def _out_arcade(self, arg: int):
        if self.state['output_state'] == 0:
            self.state['location'][0] = arg
            self.state['output_state'] = 1
        elif self.state['output_state'] == 1:
            self.state['location'][1] = arg
            self.state['output_state'] = 2
        else:
            if self.state['location'][0] == -1:
                self.state['score'] = arg
            else:
                self.state['grid'][self.state['location'][1]][self.state['location'][0]] = arg
                if arg == 3:
                    self.state['paddle'] = self.state['location'][0]
                elif arg == 4:
                    self.state['ball'] = self.state['location'][0]
                    if self.state['show_grid']:
                        self.show_grid()

            self.state['output_state'] = 0

    def _out(self, args, _):
        '''Output'''
        if self.state['type'] == 'robot':
            self._out_robot(args[0])
        elif self.state['type'] == 'arcade':
            self._out_arcade(args[0])
        else:
            self.state['outputs'].append(args[0])
        self.state['ptr'] += 2

    def _jit(self, args, _):
        '''Jump if true'''
        if args[0]:
            self.state['ptr'] = args[1]
        else:
            self.state['ptr'] += 3

    def _jif(self, args, _):
        '''Jump if false'''
        if not args[0]:
            self.state['ptr'] = args[1]
        else:
            self.state['ptr'] += 3

    def _lt(self, args, opts):
        '''Less than'''
        self.state['pgm'][opts[0]] = int(args[0] < args[1])
        self.state['ptr'] += 4

    def _eq(self, args, opts):
        '''Equals'''
        self.state['pgm'][opts[0]] = int(args[0] == args[1])
        self.state['ptr'] += 4

    def _rba(self, args, _):
        '''Equals'''
        self.state['rel'] += args[0]
        self.state['ptr'] += 2

    def intcode(self):
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

    def run(self):
        '''Run a program'''
        while self.state['ptr'] != -1:
            # print(self.state['ptr'])
            self.intcode()
            if self.state['type'] == 'iterate' and self.state['outputs']:
                return [self.state['outputs'].pop()]

        if self.state['outputs']:
            return self.state['outputs']

        return [self.state['pgm'][0]]
