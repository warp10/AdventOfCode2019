#!/usr/bin/env python3

def calculate_fuel(mass):
    return mass // 3 - 2


def calculate_total_fuel(mass):
    total_fuel = 0
    while True:
        mass = calculate_fuel(mass)
        if mass < 0:
            break
        total_fuel += mass
    return total_fuel


if __name__ == '__main__':
    with open('input_1_2.txt') as f:
        print(sum(calculate_total_fuel(int(l.strip())) for l in f.readlines()))
