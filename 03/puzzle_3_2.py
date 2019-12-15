#!/usr/bin/env python3

import collections


class Panel:
    def __init__(self, string1, string2):
        self.string1 = string1.split(',')
        self.string2 = string2.split(',')
        self.wire1_name = 'wire1'
        self.wire2_name = 'wire2'
        # Format of each element of paths_data:
        # (x, y): {wire1: 0, wire2: 1}
        # "wire2: 1" means wire2 is not there (and vicevesra for "wire2: 0")
        self.paths_data = collections.defaultdict(dict)
        # Format of each element of paths_length:
        # (x, y): {wire1: w, wire 2: z},
        # w and z are integers representing the length of the wirte at (x, y)
        self.paths_length = collections.defaultdict(dict)
        self.dispatch = {
            'R': self.go_right,
            'L': self.go_left,
            'U': self.go_up,
            'D': self.go_down,
        }

        # Format for position: (x, y)
        self.position = (0, 0)
        self.calculate_path(self.string1, self.wire1_name)
        self.position = (0, 0)
        self.calculate_path(self.string2, self.wire2_name)

        self.calculate_crossing_points()

        self.position = (0, 0)
        self.calculate_path_length(self.string1, self.wire1_name)
        self.position = (0, 0)
        self.calculate_path_length(self.string2, self.wire2_name)

    def go_right(self, number, wire_name):
        for i in range(number):
            self.position = (self.position[0] + 1, self.position[1])
            self.update_position(wire_name)

    def go_left(self, number, wire_name):
        for i in range(number):
            self.position = (self.position[0] - 1, self.position[1])
            self.update_position(wire_name)

    def go_up(self, number, wire_name):
        for i in range(number):
            self.position = (self.position[0], self.position[1] + 1)
            self.update_position(wire_name)

    def go_down(self, number, wire_name):
        for i in range(number):
            self.position = (self.position[0], self.position[1] - 1)
            self.update_position(wire_name)

    def update_position(self, wire_name):
        self.paths_data[self.position].update({wire_name: 1})

    def calculate_path(self, string, wire_name):
        for item in string:
            order, number = item[0], int(item[1:])
            self.dispatch[order](number, wire_name)

    def calculate_crossing_points(self):
        self.crossing_points = list(filter(lambda x:
            all(k in self.paths_data[x].keys() for k in ('wire1', 'wire2')),
            self.paths_data))

    def calculate_manhattan(self):
        return min(abs(cp[0]) + abs(cp[1]) for cp in self.crossing_points)

    def calculate_path_length(self, string, wire_name):
        length = 0
        for item in string:
            order, number = item[0], int(item[1:])
            for i in range(number):
                self.dispatch[order](1, wire_name)
                length += 1
                if self.position in self.crossing_points:
                    self.paths_length[self.position].update({wire_name: length})

    def calculate_shortest_path(self):
        return min(self.paths_length[item]['wire1']
        + self.paths_length[item]['wire2'] for item in self.paths_length)


if __name__ == '__main__':
    with open('input_3_1.txt') as f:
        string1 = f.readline()
        string2 = f.readline()
        panel = Panel(string1, string2)
        print(panel.calculate_shortest_path())
