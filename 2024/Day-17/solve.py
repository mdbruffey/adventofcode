import time

class Computer():
    def __init__(self, registers, program):
        self.registers = registers
        self.program = program
        self.target = program[::-1]
        self.pointer = 0
        self.output = []
        self.instructions = {0:self.adv,
                             1:self.bxl,
                             2:self.bst,
                             3:self.jnz,
                             4:self.bxc,
                             5:self.out,
                             6:self.bdv,
                             7:self.cdv}
        
    def adv(self, op): #0
        if op < 4:
            pow = op
        else:
            pow = self.registers[op-4]
        self.registers[0] = int(self.registers[0]/(2**pow))
        self.pointer += 2

    def bxl(self, op): #1
        self.registers[1] = self.registers[1] ^ op
        self.pointer += 2

    def bst(self, op): #2
        if op < 4:
            num = op
        else:
            num = self.registers[op-4]
        self.registers[1] = num % 8
        self.pointer += 2

    def jnz(self, op): #3
        if self.registers[0]:
            self.pointer = op
        else:
            self.pointer += 2

    def bxc(self, op):
        self.registers[1] = self.registers[1] ^ self.registers[2]
        self.pointer += 2

    def out(self, op):
        if op < 4:
            num = op
        else:
            num = self.registers[op-4]
        self.output.append(num%8)
        self.pointer += 2

    def bdv(self, op):
        if op < 4:
            pow = op
        else:
            pow = self.registers[op-4]
        self.registers[1] = self.registers[0]//(2**pow)
        self.pointer += 2

    def cdv(self, op):
        if op < 4:
            pow = op
        else:
            pow = self.registers[op-4]
        self.registers[2] = self.registers[0]//(2**pow)
        self.pointer += 2

    def run(self, a=0, debug=False):
        self.output = []
        self.pointer = 0
        if debug:
            self.registers = [a, 0, 0]
        while self.pointer < len(self.program):
            code = self.program[self.pointer]
            op = self.program[self.pointer+1]
            self.instructions[code](op)
        return self.output
    
    #I had to borrow this from someone. I understand conceptually what to do here, but struggled
    #to implement it myself.
    def find_a(self, a=0, depth=0):
        if depth == len(self.target):
            return a
        for i in range(8):
            result = self.run(a=a*8+i,debug=True)
            if result and result[0] == self.target[depth]:
                result = self.find_a((a*8+i), depth+1)
                if result:
                    return result
        return 0

def part1(computer):
    computer.run()
    return ",".join(map(str,computer.output))

def part2(computer):
    return computer.find_a()

with open("input.txt") as file:
    data = file.read()
registers, program = data.split("\n\n")
registers = registers.splitlines()
registers = list(map(int,[x.split(": ")[1] for x in registers]))
program = list(map(int,program.split(": ")[1].split(",")))
computer = Computer(registers, program)

start = time.perf_counter()
res1 = part1(computer)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(computer)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")