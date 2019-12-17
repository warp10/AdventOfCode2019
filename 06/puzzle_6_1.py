#!/usr/bin/env python

import collections


class Graph():
    def __init__(self, data):
        self.data = data
        self.graph = self.load_data()

    def load_data(self):
        graph = collections.defaultdict(str)
        for line in self.data:
            left, right = line.split(')')
            graph[right] = left
        return graph

    def calculate_orbits(self):
        return sum(self.iterate_planet_orbits(node)
                   for node in self.graph.keys())

    def iterate_planet_orbits(self, node):
        if node == 'COM':
            return 0
        return 1 + self.iterate_planet_orbits(self.graph[node])


if __name__ == '__main__':
    with open('input_6_1.txt', 'r') as f:
        graph = Graph(f.read().splitlines())
        print(graph.calculate_orbits())
