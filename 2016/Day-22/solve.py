import time

def neighbors(row,col,grid):
    coords = []
    for i in range(-1,2):
        newRow = row + i
        for j in range(-1,2):
            newCol = col + j
            if newCol >= 0 and newCol < len(grid[0]):
                if newRow >= 0 and newRow < len(grid):
                    if newRow != row or newCol != col:
                        if abs(newRow-row) - abs(newCol-col) != 0:
                            coords.append((newRow, newCol))
    return coords

def can_transfer(row, col, grid):
    count = 0
    for neighbor in neighbors(row, col, grid):
        i,j = neighbor
        if grid[row][col]["used"] <= grid[i][j]["avail"]:
            count += 1
    return count

def distance_to_space(start, grid):
    queue = []
    queue.append(start+(0,))
    visited = set()
    while queue:
        curr = queue.pop(0)
        row, col, steps = curr
        if grid[row][col] == "_":
            return steps
        for next in neighbors(row, col, grid):
            i, j = next
            if grid[i][j] != "#":
                if next not in [x[:-1] for x in visited]:
                    queue.append(next + (steps+1,))
                    visited.add(next + (steps+1,))


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

def part2(grid):
    viz = [['.' for _ in range(WIDTH)] for __ in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j]["size"] > 100:
                viz[i][j] = "#"
            elif grid[i][j]["used"] == 0:
                viz[i][j] = "_"
            elif can_transfer(i,j,grid):
                viz[i][j] = "*"
    viz[0][WIDTH-1] = "G"
    distance = distance_to_space((0,WIDTH-1),viz)
    return distance + (WIDTH-2)*5

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

start = time.perf_counter()
res1 = part1(grid)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(grid)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")