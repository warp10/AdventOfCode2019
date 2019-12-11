#!/usr/bin/env python3

import unittest

from puzzle_1_2 import calculate_total_fuel

class TestPuzzle01(unittest.TestCase):
    def test_calculate_fuel(self):
        self.assertEqual(calculate_total_fuel(14), 2)
        self.assertEqual(calculate_total_fuel(1969), 966)
        self.assertEqual(calculate_total_fuel(100756), 50346)

if __name__ == '__main__':
    unittest.main()