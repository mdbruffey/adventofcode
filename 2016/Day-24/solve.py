import time

def get_start(target, grid):
    index = -1
    i = 0
    while index < 0:
        if grid[i].count("0") > 0:
            index = grid[i].index("0")
            break
        i += 1
    return (i, index, 1) + tuple([0 for i in range(len(target)-1)]) + (0,)

def get_target(grid):
    total = len(grid)*len(grid[0])
    count = 0
    for row in grid:
        count += row.count("#") + row.count(".")
    num = total - count
    return tuple([1 for i in range(num)])

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

def make_move(curr, move, grid):
    steps = curr[-1]
    state = list(curr[2:-1])
    row, col = move
    index = -1
    if grid[row][col].isnumeric():
        index = int(grid[row][col])
        state[index] = 1
    return move + tuple(state) + (steps + 1,)

def weight(x, target):
    return len(target)- sum(x[2:-1])

def part1(grid):
    target = get_target(grid)
    start = get_start(target, grid)
    queue = [start]
    visited = set()
    while queue:
        curr = queue.pop(0)
        state = curr[2:-1]
        steps = curr[-1]
        if state == target:
            return steps
        for move in get_moves(curr, grid):
            next = make_move(curr, move, grid)
            if next not in visited:
                queue.append(next)
                visited.add(next)
        queue.sort(key=lambda x: weight(x, target))

def part2(grid):
    target = get_target(grid)
    start = get_start(target, grid)
    queue = [start]
    visited = set()
    while queue:
        curr = queue.pop(0)
        state = curr[2:-1]
        steps = curr[-1]
        if state == target and curr[:2] == start[:2]:
            return steps
        for move in get_moves(curr, grid):
            next = make_move(curr, move, grid)
            if next not in visited:
                queue.append(next)
                visited.add(next)

with open("input.txt") as file:
    data = file.readlines()
grid = []
for line in data:
    line = line.strip("\n")
    grid.append(list(line))

start = time.perf_counter()
#res1 = part1(grid)
#print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(grid)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")