"""CPU functionality."""

import sys

memory = [0] * 256


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.register = [0] * 8
        self.pc = 0
        self.command = {
            "HLT":  0b00000001,
            "PRN":  0b01000111,
            "LDI":  0b10000010,
            "MUL":  0b10100010,
            "ADD":  0b10100000,
            "PUSH": 0b01000101,
            "POP":  0b01000110,
        }

    def load(self):
        """Load a program into memory."""

        address = 0
        if len(sys.argv) != 2:
            print("Need proper file name passed!")
            sys.exit(1)

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]
        filename = sys.argv[1]

        with open(filename) as f:
            for line in f:
                if line == '':
                    continue
                split_line = line.split("#")
                num = split_line[0].strip()

                memory[address] = int(num)
                address += 1

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True
        pc = 0

        while running:
            command = memory[pc]

            if command == "HLT":
                running = False
                pc += 1
            elif command == "PRN":
                num = memory[pc+1]
                print(num)
                pc += 2
            # elif command == "LDI":
            # elif command == "MUL":
            elif command == "ADD":
                register1 = memory[pc + 1]
                register2 = memory[pc + 2]

                val1 = registers[register1]
                val2 = registers[register2]
                registers[register1] = val1 + val2
                pc += 3
            elif command == "PUSH":
                register = memory[pc + 1]
                registers[pointer] -= 1

                register_value = registers[register]

                memory[registers[pointer]] = register_value
                pc += 2
            elif command == "POP":
                value = memory[registers[pointer]]
                register = memory[pc + 1]

                registers[register] = value
                registers[pointer] += 1
                pc += 2
            else:
                print(f"Unknown instruction {command}")
                sys.exit(1)

    def ram_read(self, mar):
        ram = [0] * 256
        return

    def ram_write(self, mar, val):
        pass
