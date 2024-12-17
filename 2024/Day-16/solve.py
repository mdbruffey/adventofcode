import time
from queue import Queue

directions = [(1,0),(0,1),(-1,0),(0,-1)]

def get_cost(p1, p2):
    if p1[1] == p2[1]:
        return 1
    else:
        return 1001
    
def get_neighbors(pos, grid):
    dir = pos[1]
    x,y = pos[0]
    neighbors = []
    for i in range(dir-1,dir+2):
        if i == -1:
            i += 4
        dx, dy = directions[i%4]
        if grid[y+dy][x+dx] != "#":
            neighbor = ((x+dx,y+dy),i%4)
            neighbors.append(neighbor)
    return neighbors

def get_points(path, came_from):
    points = set()
    curr = [path]
    while curr:
        if len(curr) > 1:
            for op in curr:
                points.update(get_points(op, came_from))
            return points
        curr = curr[0]
        points.add(curr[0])
        curr = came_from[curr]
    return points


def part1(data):
    start = ((1, len(data)-2), 0)
    end = (len(data[0])-2, 1)
    
    frontier = Queue()
    cost_so_far = dict()
    came_from = dict()
    frontier.put(start) 
    cost_so_far[start] = 0
    came_from[start] = None
    paths = set()

    while not frontier.empty():
        curr = frontier.get()
        if curr[0] == end:
            paths.add(curr)
            continue

        for next in get_neighbors(curr, data):
            new_cost = cost_so_far[curr] + get_cost(curr,next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                came_from[next] = [curr]
                frontier.put(next)
            elif new_cost == cost_so_far[next]:
                came_from[next].append(curr)

    costs = dict()
    for path in paths:
        costs[path] = cost_so_far[path]
    best = min(costs[path] for path in paths)
    best_paths = [path for path in paths if costs[path] == best]
    return best, best_paths, came_from

def part2(best_paths, came_from, data):
    spots = set()
    for path in best_paths:
        spots.update(get_points(path, came_from))

    #print out the graph with paths marked for debugging purposes
    """for i in range(len(data)):
        for j in range(len(data[0])):
            if (j,i) in spots:
                print("O",end="")
            else:
                print(data[i][j],end="")
        print()"""
    
    return len(spots)


with open("input.txt") as file:
    data = file.read().splitlines()

start = time.perf_counter()
res1, best_paths, came_from = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(best_paths, came_from, data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")