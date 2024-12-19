import time
from queue import Queue

dirs = [(0,1),(1,0),(-1,0),(0,-1)]

def get_path(grid, size):
    start = (0,0)
    end = (size-1,size-1)
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        curr = frontier.get()
        if curr == end:
            break
        for next in get_neighbors(curr, grid, size):
            new_cost = cost_so_far[curr] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                came_from[next] = curr
                frontier.put(next)
    if curr == end:
        path = set()
        while curr:
            path.add(curr)
            curr = came_from[curr]
        return path
    return None

def get_neighbors(pos, grid, size):
    x,y = pos
    neighbors = []
    options = [(x+dx,y+dy) for dx,dy in dirs]
    for option in options:
        if option in grid:
            continue
        elif 0 <= option[0] < size and 0 <= option[1] < size:
            neighbors.append(option)
    return neighbors

def part1(data):
    fallen = 1024
    grid = set(data[:fallen])
    grid_size = 71
    start = (0,0)
    end = (grid_size-1,grid_size-1)
    frontier = Queue()
    frontier.put(start)
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        curr = frontier.get()
        if curr == end:
            break
        for next in get_neighbors(curr, grid, grid_size):
            new_cost = cost_so_far[curr] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                came_from[next] = curr
                frontier.put(next)

    return cost_so_far[end]

def part2(data, size):
    fallen = 1024
    incoming = data[fallen:]
    path = get_path(set(data[:fallen]),size)
    #this is probably not the best approach. Making part 1 faster
    #would also benefit this, I suppose
    for i in range(len(incoming)): 
        if incoming[i] in path:
            path = get_path(set(data[:fallen+i+1]),size)
            if not path:
                return f"{incoming[i][0]},{incoming[i][1]}"

with open("input.txt") as file:
    data = file.read().splitlines()
data = list(map(tuple, [map(int,line.split(",")) for line in data]))

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data, 71)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")