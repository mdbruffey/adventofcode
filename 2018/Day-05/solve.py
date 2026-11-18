import time

def part1(polymer):
    changes = True
    while changes:
        i = 0
        changes = False
        while i < len(polymer)-1:
            if abs(ord(polymer[i])-ord(polymer[i+1])) == 32:
                polymer = polymer[:i] + polymer[i+2:]
                changes = True
            else:
                i += 1
    return len(polymer), polymer

def part2(data):
    units = set(data.lower())
    min_size = len(data)
    for unit in units:
        polymer = data.replace(unit,"")
        polymer = polymer.replace(unit.upper(),"")
        size, _ = part1(polymer)
        if size < min_size:
            min_size = size
    return min_size

with open("input.txt") as file:
    data = file.read()

start = time.perf_counter()
res1, polymer = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(polymer)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")