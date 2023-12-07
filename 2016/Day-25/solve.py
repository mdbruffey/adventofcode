import time

def part1(data):
    for l in range(10000):
        signal = []
        registers = {"a":l,
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
            elif instruction == "out":
                signal.append(registers[line[1]])
                if len(signal) > 1:
                    if signal[-1] == signal[-2]:
                        break
                if len(signal) > 10:
                    return l

            i += 1 

with open("input.txt") as file:
    data = file.readlines()

instructions = []
for i in range(len(data)):
    instructions.append(data[i].strip("\n").split())
    data[i] = data[i].strip("\n").split()

start = time.perf_counter()
res1 = part1(instructions)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")