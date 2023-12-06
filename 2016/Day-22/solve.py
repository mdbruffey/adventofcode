import time

def part1(data):
    pass

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()

width, height = data[-1].split()[0].split("-")[-2:]
WIDTH = int(width[1:]) + 1
HEIGHT = int(height[1:])+1

grid = [[{} for _ in range(WIDTH)] for __ in range(HEIGHT)]
for line in data:
    line = line.split()
    line.remove("")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")