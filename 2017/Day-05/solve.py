import time

def part1(data):
    instructions = []
    for i in range(len(data)):
        instructions.append(int(data[i]))
    pos = 0
    steps = 0
    end = len(instructions)
    while pos < end:
        next = pos + instructions[pos]
        instructions[pos] += 1
        pos = next
        steps += 1
    return steps

def part2(data):
    instructions = []
    for i in range(len(data)):
        instructions.append(int(data[i]))
    pos = 0
    steps = 0
    end = len(instructions)
    while pos < end:
        offset = instructions[pos]
        next = pos + offset
        if offset >= 3:
            instructions[pos] -= 1
        else:
            instructions[pos] += 1
        pos = next
        steps += 1
    return steps

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")