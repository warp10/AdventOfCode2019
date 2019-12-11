#!/usr/bin/env python3


def calculate_fuel(mass):
    return mass // 3 - 2


def main():
    with open('input_1_1.txt') as f:
        return sum(calculate_fuel(int(l.strip()))for l in f.readlines())


if __name__ == '__main__':
    print(main())
