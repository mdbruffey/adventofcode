import time

def part1(data):
    registers = {"a":7,
                 "b":0,
                 "c": 0,
                 "d": 0}
    i = 0
    while i < len(data):
        line = data[i]
        instruction = line[0]
        if instruction == "cpy":
            if not line[1].isalpha():
                registers[line[2]] = int(line[1])
            elif line[1].isnumeric() and line[2].isnumeric():
                i += 1
                continue
            else:
                registers[line[2]] = registers[line[1]]
        elif instruction == "inc":
            registers[line[1]] += 1
        elif instruction == "dec":
            registers[line[1]] -= 1
        elif instruction == "jnz":
            if line[1].isalpha():
                val = registers[line[1]]
            else:
                val = int(line[1])
            if line[2].isalpha():
                jmp = registers[line[2]]
            else:
                jmp = int(line[2])
            if val != 0:
                i += jmp-1
        elif instruction == "tgl":
            if line[1].isnumeric():
                idx = i + int(line[1])
            else:
                idx = i + registers[line[1]]
            if idx < 0 or idx >= len(data):
                i += 1
                continue
            target = data[idx]
            if target[0] == "inc":
                target[0] = "dec"
            elif len(target) == 2:
                target[0] = "inc"
            elif target[0] == "jnz":
                target[0] = "cpy"
            else:
                target[0] = "jnz"
            data[idx] = target

        i += 1
    return registers["a"]

def part2(data):
    registers = {"a":12,
                 "b":0,
                 "c": 0,
                 "d": 0}
    i = 0
    while i < len(data):
        line = data[i]
        instruction = line[0]
        if instruction == "cpy":
            if not line[1].isalpha():
                registers[line[2]] = int(line[1])
            elif line[1].isnumeric() and line[2].isnumeric():
                i += 1
                continue
            else:
                registers[line[2]] = registers[line[1]]
        elif instruction == "inc":
            registers[line[1]] += 1
        elif instruction == "dec":
            registers[line[1]] -= 1
        elif instruction == "jnz":
            if line[1].isalpha():
                val = registers[line[1]]
            else:
                val = int(line[1])
            if line[2].isalpha():
                jmp = registers[line[2]]
            else:
                jmp = int(line[2])
            if val != 0:
                i += jmp-1
        elif instruction == "tgl":
            if line[1].isnumeric():
                idx = i + int(line[1])
            else:
                idx = i + registers[line[1]]
            if idx < 0 or idx >= len(data):
                i += 1
                continue
            target = data[idx]
            if target[0] == "inc":
                target[0] = "dec"
            elif len(target) == 2:
                target[0] = "inc"
            elif target[0] == "jnz":
                target[0] = "cpy"
            else:
                target[0] = "jnz"
            data[idx] = target

        i += 1
    return registers["a"]

with open("input.txt") as file:
    data = file.readlines()

instructions = []
for i in range(len(data)):
    instructions.append(data[i].strip("\n").split())
    data[i] = data[i].strip("\n").split()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(instructions)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")