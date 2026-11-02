import time

def part1(data):
    i = 0
    depth = 0
    values = {}
    garbage = False
    while i < len(data):
        if data[i] == "!":
            i += 2
            continue
        if data[i] == "<" and not garbage:
            garbage = True
        elif data[i] == ">":
            garbage = False
        elif data[i] == "{" and not garbage:
            depth += 1
        elif data[i] == "}" and not garbage:
            depth -= 1
            values[depth] = values.setdefault(depth, 0) + 1
        i += 1
    return sum([(i+1)*v for i,v in values.items()])

def part2(data):
    i = 0
    count = 0
    garbage = False
    while i < len(data):
        if data[i] == "!":
            i += 2
            continue
        if data[i] == "<" and not garbage:
            garbage = True
        elif data[i] == ">":
            garbage = False
        elif garbage:
            count += 1
        i += 1
    return count

with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")