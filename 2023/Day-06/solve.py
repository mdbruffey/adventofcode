import time
import math

def find_wins(T, record):
    t1 = (T + math.sqrt(T**2 - 4*record))//2
    t2 = (T - math.sqrt(T**2 - 4*record))//2
    return int(abs(t2-t1))

def part1(data):
    ways = []
    for key, value in data.items():
        ways.append(find_wins(key, value))
    return math.prod(ways)

def part2(data):
    T = int(''.join(map(str,data.keys())))
    record = int(''.join(map(str,data.values())))
    return find_wins(T, record)

with open("input.txt") as file:
    data = file.readlines()

for i, line in enumerate(data):
    line = line.strip("\n").split(":")[1].split()
    data[i] = line
times = data[0]
records = data[1]
races = {}
for i in range(len(times)):
    races[int(times[i])] = int(records[i])
print(races)

start = time.perf_counter()
res1 = part1(races)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(races)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")