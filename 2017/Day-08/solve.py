import time

comparisons = {
    "<": lambda a,b:  a < b,
    ">": lambda a,b: a > b,
    "==": lambda a,b: a == b,
    "!=": lambda a,b: a != b,
    "<=": lambda a,b: a <= b,
    ">=": lambda a,b: a >= b
}

class CPU():
    def __init__(self):
        self.registers = {}
        self.highest = 0

    def execute(self, instruction):
        result, comparison = instruction.split(" if ")
        reg, inst, val = result.split()
        register, op, num = comparison.split()
        if comparisons[op](self.registers.get(register, 0),int(num)): #just learned about the .get() method of dictionaries a couple days ago; it's awesome!
            if inst == "inc":
                val = self.registers.get(reg,0) + int(val)
                self.registers[reg] = val
            else:
                val = self.registers.get(reg,0) - int(val)
                self.registers[reg] = val
            if val > self.highest: #just catching part 2 right here while we're at it
                self.highest = val

def part1(data):
    computer = CPU()
    for line in data:
        computer.execute(line)
    return max(computer.registers.values()), computer.highest


with open("input.txt") as file:
    data = file.read().splitlines()

start = time.perf_counter()
res1, res2 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
#res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")