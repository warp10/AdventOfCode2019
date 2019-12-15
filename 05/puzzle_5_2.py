#! /usr/bin/env python3


class Intcode():
    def do_sum(self):
        a = self.get_argument(self.ip+1, self.mode1)
        b = self.get_argument(self.ip+2, self.mode2)
        res = self.opcodes[self.ip+3]

        self.opcodes[res] = a + b
        self.ip += 4

    def do_multiply(self):
        a = self.get_argument(self.ip+1, self.mode1)
        b = self.get_argument(self.ip+2, self.mode2)
        res = self.opcodes[self.ip+3]

        self.opcodes[res] = a * b
        self.ip += 4

    def save_value(self):
        res = self.opcodes[self.ip+1]
        inp = input("Enter input: ")

        self.opcodes[res] = int(inp)
        self.ip += 2

    def output_value(self):
        res = self.get_argument(self.ip+1, self.mode1)

        print(res)
        self.ip += 2

    def jump_if_true(self):
        a = self.get_argument(self.ip+1, self.mode1)
        b = self.get_argument(self.ip+2, self.mode2)

        self.ip = b if a else self.ip+3

    def jump_if_false(self):
        a = self.get_argument(self.ip+1, self.mode1)
        b = self.get_argument(self.ip+2, self.mode2)

        self.ip = b if not a else self.ip+3

    def less_than(self):
        a = self.get_argument(self.ip+1, self.mode1)
        b = self.get_argument(self.ip+2, self.mode2)
        res = self.opcodes[self.ip+3]

        self.opcodes[res] = 1 if a < b else 0
        self.ip += 4

    def equals(self):
        a = self.get_argument(self.ip+1, self.mode1)
        b = self.get_argument(self.ip+2, self.mode2)
        res = self.opcodes[self.ip+3]

        self.opcodes[res] = 1 if a == b else 0
        self.ip += 4

    def __init__(self, string):
        self.opcodes = self.load_program(string)
        self.ip = 0
        self.dispatch = {
            1: self.do_sum,
            2: self.do_multiply,
            3: self.save_value,
            4: self.output_value,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
        }
        # Not really used, but might be useful in the future
        self.mode_mapping = {
            0: 'position',
            1: 'immediate',
        }

    def get_argument(self, ip, mode):
        if mode == 0:
            return self.opcodes[self.opcodes[ip]]
        else:
            return self.opcodes[ip]

    def load_program(self, string):
        return list(map(int, string.split(",")))

    def dump_program(self):
        return ','.join(map(str, self.opcodes))

    def parse_opcode(self, opcode):
        opcode = str(opcode).zfill(5)
        self.opcode = int(opcode[-2:])
        self.mode1 = int(opcode[2])
        self.mode2 = int(opcode[1])
        self.mode3 = int(opcode[0])

    def run_program(self):
        while True:
            opcode = self.opcodes[self.ip]
            self.parse_opcode(opcode)

            if self.opcode == 99:
                break

            self.dispatch[self.opcode]()

    def get_first_opcode(self):
        return self.opcodes[0]


if __name__ == '__main__':
    with open('input_5_2.txt') as f:
        intcode = Intcode(f.read())
        intcode.run_program()
