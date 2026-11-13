import time

class Machine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = {}
        self.pos = 0
        self.mul_count = 0

    def set(self, register, value):
        if value.isalpha():
            self.registers[register] = self.registers[value]
        else:
            self.registers[register] = int(value)

    def add(self, register, value):
        if value.isalpha():
            self.registers[register] = self.registers.setdefault(register, 0) + self.registers.setdefault(value, 0)
        else:
            self.registers[register] = self.registers.setdefault(register, 0) + int(value)

    def sub(self, register, value):
        if value.isalpha():
            self.registers[register] = self.registers.setdefault(register, 0) - self.registers.setdefault(value, 0)
        else:
            self.registers[register] = self.registers.setdefault(register, 0) - int(value)

    def mul(self, register, value):
        if value.isalpha():
            self.registers[register] = self.registers.setdefault(register, 0) * self.registers.setdefault(value, 0)
        else:
            self.registers[register] = self.registers.setdefault(register, 0) * int(value)

    def mod(self, register, value):
        if value.isalpha():
            self.registers[register] = self.registers.setdefault(register, 0) % self.registers.setdefault(value, 0)
        else:
            self.registers[register] = self.registers.setdefault(register, 0) % int(value)

    def jgz(self, register, value):
        if register.isalpha() and self.registers.setdefault(register, 0) > 0:
            if value.isalpha():
                self.pos += self.registers.setdefault(value, 0)
            else:
                self.pos += int(value)
        elif register.isnumeric() and int(register) > 0:
            if value.isalpha():
                self.pos += self.registers.setdefault(value, 0)
            else:
                self.pos += int(value)
        else:
            self.pos += 1

    def jnz(self, register, value):
        if register.isalpha() and self.registers.setdefault(register, 0) != 0:
            if value.isalpha():
                self.pos += self.registers.setdefault(value, 0)
            else:
                self.pos += int(value)
        elif register.isnumeric() and int(register) != 0:
            if value.isalpha():
                self.pos += self.registers.setdefault(value, 0)
            else:
                self.pos += int(value)
        else:
            self.pos += 1

    def run(self):
        while self.pos >= 0 and self.pos < len(self.instructions):
            inst, params = self.instructions[self.pos]
            if inst == "set":
                self.set(params[0],params[1])
            if inst == "add":
                self.add(params[0], params[1])
            if inst == "sub":
                self.sub(params[0], params[1])
            if inst == "mul":
                self.mul(params[0], params[1])
                self.mul_count += 1
            if inst == "mod":
                self.mod(params[0], params[1])
            if inst == "jgz":
                self.jgz(params[0], params[1])
                continue
            if inst == "jnz":
                self.jnz(params[0], params[1])
                continue
            self.pos += 1
        return 1

def part1(instructions):
    prog = Machine(instructions)
    prog.run()
    return prog.mul_count

def part2(instructions):
    prog = Machine(instructions[:8])
    prog.registers["a"] = 1
    #initialize the values of b and c
    prog.run() 
    b = prog.registers["b"]
    c = prog.registers["c"]
    increment = abs(int(instructions[-2][1][1]))
    composites = 0
    while True:
        for i in range(2,round(b**0.5)):
            if b % i == 0:
                composites += 1
                break        
        if b == c:
            break
        b += increment
    return composites

with open("input.txt") as file:
    data = file.read().split("\n")

instructions = []
for line in data:
    line = line.split()
    inst = line[0]
    params = line[1:]
    instructions.append((inst, params))

start = time.perf_counter()
res1 = part1(instructions)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(instructions)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")