import time
from math import lcm

def part1(data):
    danger = 0
    for t in range(max(data.keys())+1):
        
        if t in data.keys() and t % (2*(data[t]-1)) == 0:
            danger += t*data[t]
    return danger

def part2(data):
    step = 1
    danger = 1
    wait = 0
    while danger > 0:
        wait += step
        danger = 0
        for t in range(wait, max(data.keys())+1 + wait):
            if t-wait in data.keys() and t % (2*(data[t-wait]-1)) == 0:
                danger += t*data[t-wait]
                break
    return wait

with open("input.txt") as file:
    data = file.read().split("\n")

layers = {}
for line in data:
    depth, length = line.split(": ")
    layers[int(depth)] = int(length)

start = time.perf_counter()
res1 = part1(layers)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(layers)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")