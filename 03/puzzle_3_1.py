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

    def calculate_manhattan(self):
        crossing_point = filter(lambda x:
            all(k in self.paths_data[x].keys() for k in ('wire1', 'wire2')),
            self.paths_data)
        return min(abs(cp[0]) + abs(cp[1]) for cp in crossing_point)

if __name__ == '__main__':
    with open('input_3_1.txt') as f:
        string1 = f.readline()
        string2 = f.readline()
        panel = Panel(string1, string2)
        print(panel.calculate_manhattan())
