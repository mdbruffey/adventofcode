import time
import re

def part1(data):
    ranges = [(int(x),int(y)) for x,y in map(lambda x: x.split("-"), data)]
    count = 0
    for x,y in ranges:
        for i in range(x, y+1):
            string = str(i)
            mid = len(string)//2
            if string[:mid] == string[mid:]:
                count += i
    return count

def part2(data):
    ranges = [(int(x),int(y)) for x,y in map(lambda x: x.split("-"), data)]
    count = 0
    for x,y in ranges:
        for i in range(x, y+1):
            if re.match(r"^(\d+)\1+$", str(i)):
                count += i
    return count

with open("input.txt") as file:
    data = file.read().split(",")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")