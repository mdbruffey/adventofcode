import time

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

def part1(grid):
    bursts = 10000
    infected = set()
    dir = 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "#":
                infected.add((i,j))
    curr = (len(grid)//2, len(grid)//2)
    for _ in range(bursts):
        if curr in infected:
            dir += 1
            infected.remove(curr)
        else:
            dir -= 1
            infected.add(curr)
            count += 1
        di, dj = dirs[dir%4]
        curr = (curr[0] + di, curr[1] + dj)
    return count

def part2(grid):
    bursts = 10000
    infected = set()
    weakened = set()
    flagged = set()
    dir = 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "#":
                infected.add((i,j))
    curr = (len(grid)//2, len(grid)//2)
    for _ in range(bursts):
        if curr in infected:
            dir += 1
            infected.remove(curr)
            flagged.add(curr)
        elif curr in weakened:
            infected.add(curr)
            count += 1
        elif curr in flagged:
            dir += 2
            flagged.remove(curr)
        else:
            dir -= 1
            weakened.add(curr)
        di, dj = dirs[dir%4]
        curr = (curr[0] + di, curr[1] + dj)
    return count

with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")