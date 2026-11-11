import time

class Machine:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = {}
        self.pos = 0
        self.last_played = None

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

    def snd(self, value):
        if value.isalpha():
            if self.registers.setdefault(value, 0):
                self.last_played = self.registers[value]
        else:
            if int(value) > 0:
                self.last_played

    def rcv(self, register):
        if self.registers.setdefault(register, 0):
            return self.last_played

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

    def run(self):
        while self.pos >= 0 and self.pos < len(self.instructions):
            inst, params = self.instructions[self.pos]
            if inst == "set":
                self.set(params[0],params[1])
            if inst == "add":
                self.add(params[0], params[1])
            if inst == "mul":
                self.mul(params[0], params[1])
            if inst == "mod":
                self.mod(params[0], params[1])
            if inst == "snd":
                self.snd(params[0])
            if inst == "rcv":
                recovered = self.rcv(params[0])
                if recovered:
                    return recovered
            if inst == "jgz":
                self.jgz(params[0], params[1])
                continue
            self.pos += 1
        return None

class Machine2:
    def __init__(self, instructions, id):
        self.instructions = instructions
        self.registers = {"p": id}
        self.queue = []
        self.pos = 0
        self.sent = 0
        self.target = None
        self.waiting = False
        self.terminated = False

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

    def snd(self, value):
        if value.isalpha():
            self.target.queue.append(self.registers.setdefault(value, 0))
        else:
            self.target.queue.append(int(value))
        self.sent += 1

    def rcv(self, register):
        if len(self.queue):
            value = self.queue[0]
            self.registers[register] = value
            if len(self.queue) > 1:
                self.queue = self.queue[1:]
            else:
                self.queue = []
            self.waiting = False
        else:
            self.waiting = True

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

    def step(self):
        if self.terminated:
            return 0
        inst, params = self.instructions[self.pos]
        if inst == "set":
            self.set(params[0],params[1])
        if inst == "add":
            self.add(params[0], params[1])
        if inst == "mul":
            self.mul(params[0], params[1])
        if inst == "mod":
            self.mod(params[0], params[1])
        if inst == "snd":
            self.snd(params[0])
        if inst == "rcv":
            self.rcv(params[0])
        if inst == "jgz":
            self.jgz(params[0], params[1])
            return 1
        if not self.waiting:
            self.pos += 1
        if self.pos >= len(instructions) or self.pos < 0:
            self.terminated = True
            self.waiting = True
        return 1

def part1(data):
    machine = Machine(data)
    return machine.run()

def part2(data):
    prog1 = Machine2(data, 0)
    prog2 = Machine2(data, 1)
    prog1.target = prog2
    prog2.target = prog1
    while True:
        if (prog1.waiting and prog2.waiting) or \
            (prog1.terminated and prog2.terminated) or \
            (prog1.waiting and prog2.terminated) or \
            (prog1.terminated and prog2.waiting):
            break
        prog1.step()
        prog2.step()
    return prog2.sent

with open("input.txt") as file:
    data = file.read().split("\n")

instructions = []
for line in data:
    inst = line.split()[0]
    params = line.split()[1:]
    instructions.append([inst, params])

start = time.perf_counter()
res1 = part1(instructions)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(instructions)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")