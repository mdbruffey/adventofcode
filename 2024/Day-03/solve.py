import time
import re

def part1(data):
    ops = re.findall(r"mul\(\d+,\d+\)", data)
    reg = 0
    for op in ops:
        x,y = map(int,op[4:-1].split(","))
        reg += x*y
    return reg

def part2(data):
    data = data.split("don't()")
    instructions = data[0]
    for entry in data:
        i = entry.find("do()")
        if i >=0:
            entry = entry[i+4:]
            instructions += entry
    return part1(instructions)


with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")