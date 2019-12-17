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

    def iterate_planet_orbits(self, node):
        if node == 'COM':
            return [node]
        return [node] + self.iterate_planet_orbits(self.graph[node])

    def calculate_minimum_transfers(self):
        you_path = self.iterate_planet_orbits('YOU')
        santa_path = self.iterate_planet_orbits('SAN')
        join = next((y for y in you_path if y in set(santa_path)), None)
        return you_path.index(join) + santa_path.index(join) - 2


if __name__ == '__main__':
    with open('input_6_2.txt', 'r') as f:
        graph = Graph(f.read().splitlines())
        print(graph.calculate_minimum_transfers())
