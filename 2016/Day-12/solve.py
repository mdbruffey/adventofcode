import time

def part1(data):
    registers = {"a": 0,
                 "b": 0,
                 "c": 0,
                 "d": 0}
    i = 0
    while i < len(data):
        line = data[i].strip("\n").split()
        instruction = line[0]
        if instruction == "cpy":
            if line[1].isnumeric():
                registers[line[2]] = int(line[1])
            else:
                registers[line[2]] = registers[line[1]]
        elif instruction == "inc":
            registers[line[1]] += 1
        elif instruction == "dec":
            registers[line[1]] -= 1
        elif instruction == "jnz":
            if line[1].isnumeric():
                val = int(line[1])
            else:
                val = registers[line[1]]
            if val != 0:
                i += int(line[2])-1
        i += 1
    return registers["a"]

def part2(data):
    registers = {"a": 0,
                 "b": 0,
                 "c": 1,
                 "d": 0}
    i = 0
    while i < len(data):
        line = data[i].strip("\n").split()
        instruction = line[0]
        if instruction == "cpy":
            if line[1].isnumeric():
                registers[line[2]] = int(line[1])
            else:
                registers[line[2]] = registers[line[1]]
        elif instruction == "inc":
            registers[line[1]] += 1
        elif instruction == "dec":
            registers[line[1]] -= 1
        elif instruction == "jnz":
            if line[1].isnumeric():
                val = int(line[1])
            else:
                val = registers[line[1]]
            if val != 0:
                i += int(line[2])-1
        i += 1
    return registers["a"]

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")