#!/usr/bin/env python3

import unittest

from puzzle_6_2 import Graph


class TestPuzzle6_2(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        data = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I",
                "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
        self.graph = Graph(data)

    def test_calculate_minimum_transfers(self):
        self.assertEqual(self.graph.calculate_minimum_transfers(), 4)


if __name__ == '__main__':
    unittest.main()
