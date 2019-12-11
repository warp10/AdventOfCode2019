#!/usr/bin/env python3

import unittest

from puzzle_1_1 import calculate_fuel


class TestPuzzle01(unittest.TestCase):
    def test_calculate_fuel(self):
        self.assertEqual(calculate_fuel(12), 2)
        self.assertEqual(calculate_fuel(14), 2)
        self.assertEqual(calculate_fuel(1969), 654)
        self.assertEqual(calculate_fuel(100756), 33583)


if __name__ == '__main__':
    unittest.main()
