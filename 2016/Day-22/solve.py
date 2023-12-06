import time

def find_pairs(row,col,grid):
    curr = grid[row][col]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if curr["used"] != 0 and curr != grid[i][j]:
                if curr["used"] <= grid[i][j]["avail"]:
                    count += 1
    return count
        

def part1(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count += find_pairs(i,j,grid)
    return count

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()

width, height = data[-1].split()[0].split("-")[-2:]
WIDTH = int(width[1:]) + 1
HEIGHT = int(height[1:])+1

grid = [[{} for _ in range(WIDTH)] for __ in range(HEIGHT)]
for line in data[2:]:
    line = line.split()
    line = [x for x in line if x != '']
    x,y = line[0].split("-")[-2:]
    x = int(x[1:])
    y = int(y[1:])
    grid[y][x]["size"] = int(line[1][:-1])
    grid[y][x]["used"] = int(line[2][:-1])
    grid[y][x]["avail"] = int(line[3][:-1])
    grid[y][x]["use%"] = int(line[4][:-1])
print(grid[1][1])

start = time.perf_counter()
res1 = part1(grid)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(grid)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")