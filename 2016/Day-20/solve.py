import time

def part1(ranges):
    ranges.sort(key=lambda x: x[0])
    upper = 0
    for i, thing in enumerate(ranges):
        a,b = thing
        if b+1 < ranges[i+1][0] and b+1 > upper:
            return b+1
        if b > upper:
            upper = b

def part2(ranges):
    ranges.sort(key=lambda x: x[0])
    upper = 0
    allowed = []
    for i in range(len(ranges)-1):
        b = ranges[i][1]
        if b > upper:
            upper = b
        if upper+1 < ranges[i+1][0]:
            allowed.extend(range(upper+1, ranges[i+1][0]))
    return len(allowed)

with open("input.txt") as file:
    data = file.readlines()

ranges = []
for line in data:
    line = line.strip("\n")
    a, b = map(int,line.split("-"))
    ranges.append([a,b])

start = time.perf_counter()
res1 = part1(ranges)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(ranges)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")