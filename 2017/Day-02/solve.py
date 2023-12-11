import time

def find_dividend(line):
    for i in range(len(line)-1):
        for j in range(i+1,len(line)):
            if line[i]%line[j] == 0:
                return line[i]//line[j]
            elif line[j]%line[i] == 0:
                return line[j]//line[i]

def part1(data):
    count = 0
    for line in data:
        print(line)
        count += max(line)-min(line)
    return count

def part2(data):
    count = 0
    for line in data:
        count += find_dividend(line)
    return count

with open("input.txt") as file:
    data = file.read()

lines = []

for line in data.split("\n"):
    lines.append(list(map(int,line.split())))

start = time.perf_counter()
res1 = part1(lines)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(lines)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")