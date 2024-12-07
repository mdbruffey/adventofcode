import time
import multiprocessing as mp
from tqdm import tqdm

directions = [(0,-1),
              (1,0),
              (0,1),
              (-1,0)]

cursor = ["^",">","v","<"]

def get_start(grid):
    start = None
    dir = None
    for i,line in enumerate(grid):
        for j in range(len(line)):
            if line[j] in cursor:
                start = (j,i)
                dir = directions[cursor.index(line[j])]
                break
        if start:
            break
    return start, dir

def move(pos,dir,grid,block=None):
    x,y = pos
    x2,y2 = x+dir[0],y+dir[1]
    if x2 >= 0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid):
        if (grid[y2][x2] == "#") or (x2,y2) == block:
            dir = directions[(directions.index(dir)+1)%4]
            return (x,y),dir
    return (x2,y2),dir

def simulate(start, dir, grid, block):
    visited = set((start, dir))
    pos = start
    while True:
        pos, ndir = move(pos, dir, grid, block)
        if pos[0] < 0 or pos[0] >= len(grid[0]) or pos[1] < 0 or pos[1] >= len(grid):
            break
        if ndir != dir: #only check for loop when direction changes
            if (pos,ndir) in visited: #if position and orientation has been seen before, it's a loop
                return True
        dir = ndir
        visited.add((pos,dir))
    return False

def m_simulate(args):
    start, dir, grid, block = args
    visited = set((start, dir))
    pos = start
    while True:
        pos, ndir = move(pos, dir, grid, block)
        if pos[0] < 0 or pos[0] >= len(grid[0]) or pos[1] < 0 or pos[1] >= len(grid):
            break
        if ndir != dir: #only check for loop when direction changes
            if (pos,ndir) in visited: #if position and orientation has been seen before, it's a loop
                return True
        dir = ndir
        visited.add((pos,dir))
    return False

def part1(grid):
    start, dir = get_start(grid)
    visited = {start,}
    pos = start
    while True:
        pos,dir = move(pos,dir,grid)
        if pos[0] < 0 or pos[0] >= len(grid[0]) or pos[1] < 0 or pos[1] >= len(grid):
            break
        visited.add(pos)
    return len(visited), visited

def part2(grid, path):
    start, dir = get_start(grid)
    count = 0
    path.remove(start)
    for pos in path:
        count += simulate(start, dir, grid, pos)
    return count

def part2_multi(grid, path):
    def states():
        for block in path:
            yield start, dir, grid, block

    start, dir = get_start(grid)
    path.discard(start)
    with mp.Pool(mp.cpu_count()) as pool:
        tasks = pool.imap_unordered(m_simulate,states())
        return print(f"Part 2b: {sum(tqdm(tasks, total=len(visited)))}",end="")

if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read().splitlines()
    start = time.perf_counter()
    res1, visited = part1(data)
    print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
    start = time.perf_counter()
    res2 = part2(data, visited)
    print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")
    start = time.perf_counter()
    res2 = part2_multi(data, visited)
    print(f" -- {time.perf_counter()-start:.4f} s")