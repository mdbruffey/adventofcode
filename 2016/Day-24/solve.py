import time
import itertools

def get_moves(curr, grid):
    moves = []
    row, col = curr[:2]
    for i in range(-1,2):
        newRow = i + row
        for j in range(-1,2):
            newCol = j + col
            if newRow >= 0 and newRow < len(grid):
                if newCol >= 0 and newCol < len(grid[0]):
                    if not (newCol != col and newRow != row):
                        if grid[newRow][newCol] != "#":
                            if newCol == col and newRow == row:
                                continue
                            else:
                                moves.append((newRow, newCol))
    return moves

def get_distance(start, target, grid):
    index = -1
    i = 0
    while index < 0:
        if grid[i].count(start) > 0:
            index = grid[i].index(start)
            break
        i += 1
    start = (i,index,0)
    queue = [start]
    visited = set()
    while queue:
        curr = queue.pop(0)
        i,j = curr[:-1]
        steps = curr[-1]
        if grid[i][j] == target:
            return steps
        for move in get_moves(curr, grid):
            if move not in visited:
                visited.add(move)
                queue.append(move + (steps+1,))

def path_distance(path, distances, min_distance):
    steps = 0
    for i in range(len(path)-1):
        pair = [path[i],path[i+1]]
        pair.sort()
        steps += distances[tuple(pair)]
        if steps > min_distance:
            return 100000
    return steps

def part1(distances):
    min_steps = 100000
    for perm in itertools.permutations(map(str,range(1,8))):
        perm = ("0",) + perm
        steps = path_distance(perm, distances, min_steps)
        if steps < min_steps:
            min_steps = steps
    
    return min_steps

def part2(distances):
    min_steps = 100000
    for perm in itertools.permutations(map(str,range(1,8))):
        perm = ("0",) + perm + ("0",)
        steps = path_distance(perm, distances, min_steps)
        if steps < min_steps:
            min_steps = steps
    
    return min_steps

with open("input.txt") as file:
    data = file.readlines()
grid = []
for line in data:
    line = line.strip("\n")
    grid.append(list(line))


distances = {}
for combo in itertools.combinations(map(str,range(8)), 2):
    distances[combo] = get_distance(*combo, grid)

start = time.perf_counter()
res1 = part1(distances)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(distances)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")