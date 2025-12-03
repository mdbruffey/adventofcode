import time

def part1(data):
    joltage = 0
    for line in data:
        high = max(line)
        idx = line.find(high)
        if idx == len(line)-1:
            joltage += int(max(line[:-1]) + high)
        else:
            joltage += int(high + max(line[idx+1:]))
    return joltage

def part2(data):
    joltage = 0
    for line in data:
        num = ""
        idx = -1
        for i in range(11, -1, -1):
            sub = line[idx+1:len(line)-i]
            next = max(sub)
            idx += sub.find(next) + 1
            num += next
        joltage += int(num)
    return joltage
            

with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")