#!/usr/bin/env python3

import unittest

from puzzle_6_1 import Graph


class TestPuzzle6_1(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        data = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I",
                "E)J", "J)K", "K)L"]
        self.graph = Graph(data)

    def test_load_data(self):
        self.assertEqual(
            self.graph.graph,
            {'B': 'COM', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E', 'G': 'B',
             'H': 'G', 'I': 'D', 'J': 'E', 'K': 'J', 'L': 'K'}
        )

    def test_calculate_orbits(self):
        self.assertEqual(self.graph.calculate_orbits(), 42)


if __name__ == '__main__':
    unittest.main()
