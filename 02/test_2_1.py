#!/usr/bin/env python3

import unittest

from puzzle_2_1 import process_program, parse_input


class TestPuzzle2_1(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(parse_input('1,0,0,0,99'), [1, 0, 0, 0, 99])
        self.assertEqual(parse_input('2,3,0,3,99'), [2, 3, 0, 3, 99])
        self.assertEqual(parse_input('2,4,4,5,99,0'), [2, 4, 4, 5, 99, 0])
        self.assertEqual(parse_input('1,1,1,4,99,5,6,0,99'),
                         [1, 1, 1, 4, 99, 5, 6, 0, 99])

    def test_process_program(self):
        self.assertEqual(process_program('1,0,0,0,99'), '2,0,0,0,99')
        self.assertEqual(process_program('2,3,0,3,99'), '2,3,0,6,99')
        self.assertEqual(process_program('2,4,4,5,99,0'), '2,4,4,5,99,9801')
        self.assertEqual(process_program('1,1,1,4,99,5,6,0,99'),
                         '30,1,1,4,2,5,6,0,99')


if __name__ == '__main__':
    unittest.main()
