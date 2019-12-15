#!/usr/bin/env python3

import unittest

from puzzle_5_1 import Intcode


class TestPuzzle2_1(unittest.TestCase):
    def test_load_and_dump_program(self):
        intcode = Intcode('1,0,0,0,99')
        self.assertEqual(intcode.dump_program(), '1,0,0,0,99')

        intcode = Intcode('2,3,0,3,99')
        self.assertEqual(intcode.dump_program(), '2,3,0,3,99')

        intcode = Intcode('2,4,4,5,99,0')
        self.assertEqual(intcode.dump_program(), '2,4,4,5,99,0')

        intcode = Intcode('1,1,1,4,99,5,6,0,99')
        self.assertEqual(intcode.dump_program(), '1,1,1,4,99,5,6,0,99')

    def test_run_program(self):
        intcode = Intcode('1,0,0,0,99')
        intcode.run_program()
        self.assertEqual(intcode.dump_program(), '2,0,0,0,99')

        intcode = Intcode('2,3,0,3,99')
        intcode.run_program()
        self.assertEqual(intcode.dump_program(), '2,3,0,6,99')

        intcode = Intcode('2,4,4,5,99,0')
        intcode.run_program()
        self.assertEqual(intcode.dump_program(), '2,4,4,5,99,9801')

        intcode = Intcode('1,1,1,4,99,5,6,0,99')
        intcode.run_program()
        self.assertEqual(intcode.dump_program(), '30,1,1,4,2,5,6,0,99')

        intcode = Intcode('3,0,4,0,99')
        intcode.run_program()

    def test_2_1program(self):
        with open('input_2_1.txt') as f:
            intcode = Intcode(f.read())
            intcode.run_program()
            self.assertEqual(intcode.get_first_opcode(), 3716293)


if __name__ == '__main__':
    unittest.main()
