#! /usr/bin/env python3


def parse_input(string):
    return list(map(int, string.split(",")))


def run_program(opcodes):
    ip = 0

    while True:
        opcode = opcodes[ip]

        if opcode == 99:
            return ','.join(list(map(str, opcodes)))

        a = opcodes[ip+1]
        b = opcodes[ip+2]
        res = opcodes[ip+3]

        if opcode == 1:
            opcodes[res] = opcodes[a] + opcodes[b]
        elif opcode == 2:
            opcodes[res] = opcodes[a] * opcodes[b]

        ip += 4


def process_program(string):
    opcodes = parse_input(string)
    opcodes = run_program(opcodes)
    return opcodes


if __name__ == '__main__':
    with open('input_2_1.txt') as f:
        print(process_program(f.read().strip()).split(',')[0])

