import time

dirs = {
        "n": (0,1),
        "ne": (1,0),
        "se": (1,-1),
        "s": (0,-1),
        "sw": (-1,0),
        "nw": (-1,1),
        }

def part1(data):
    cur = (0,0)
    for dir in data:
        step = dirs[dir]
        cur = (cur[0] + step[0], cur[1] + step[1])
    return distance(cur)

def distance(point):
    return max(abs(point[0]), abs(point[1]), abs(point[0]+point[1]))

def part2(data):
    cur = (0,0)
    furthest = 0
    for dir in data:
        step = dirs[dir]
        cur = (cur[0] + step[0], cur[1] + step[1])
        dist = distance(cur)
        if dist > furthest:
            furthest = dist
    return furthest

with open("input.txt") as file:
    data = file.read().strip().split(",")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")