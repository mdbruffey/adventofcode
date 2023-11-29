import time

def part1(data):
    count = 0
    for tri in data:
        tri.sort()
        if tri[0] + tri[1] > tri[2]:
            count += 1
    return count

def part2(data):
    count = 0
    for tri in data:
        tri.sort()
        if tri[0] + tri[1] > tri[2]:
            count += 1
    return count

with open("input.txt") as file:
    raw = file.readlines()

data = []
for line in raw:
    line = line.strip().split("  ")
    if "" in line:
        line.remove("")
    line = list(map(int, line))
    data.append(line)

triangles = []
for i in range(0, len(data), 3):
    triangles.append([data[i][0],data[i+1][0],data[i+2][0]])
    triangles.append([data[i][1],data[i+1][1],data[i+2][1]])
    triangles.append([data[i][2],data[i+1][2],data[i+2][2]])


start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(triangles)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")