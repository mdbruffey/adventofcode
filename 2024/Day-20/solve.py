import time
from queue import PriorityQueue

directions = [(1,0),(0,1),(-1,0),(0,-1)]

def manhattan(p1, p2):
    return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])

def get_neighbors(pos, walls, size, ignore):
    x,y = pos
    neighbors = []
    for neighbor in [(x+dx, y+dy) for dx,dy in directions]:
        if neighbor == ignore:
            neighbors.append(neighbor)
        elif neighbor in walls:
            continue
        elif 0 <= neighbor[0] < size[0] and 0 <= neighbor[1] < size[1]:
            neighbors.append(neighbor)
    return neighbors

def find_path(start, end, walls, size, ignore=None):
    queue = PriorityQueue()
    comes_from = dict()
    cost_till_now = dict()
    comes_from[start] = None
    cost_till_now[start] = 0
    queue.put(start,0)
    while not queue.empty():
        curr = queue.get()
        if curr == end:
            break
        for next in get_neighbors(curr, walls, size, ignore):
            new_cost = cost_till_now[curr] + 1
            if next not in cost_till_now or new_cost < cost_till_now[next]:
                cost_till_now[next] = new_cost
                comes_from[next] = curr
                priority = new_cost + abs(end[0]-next[0]) + abs(end[1]-next[1])
                queue.put(next, priority)
    path = []
    while curr:
        path.append(curr)
        curr = comes_from[curr]
    path.reverse()
    return path

def part1(data):
    cheat_time = 2
    cutoff = 100
    walls = set()
    size = (len(data[0]),len(data))
    for i in range(size[1]):
        for j in range(size[0]):
            if data[i][j] == "#":
                walls.add((j,i))
            elif data[i][j] == "S":
                start = (j,i)
            elif data[i][j] == "E":
                end = (j,i)
    path = find_path(start, end, walls, size)
    count = 0
    i = 0
    while i < len(path)-cutoff:
        j = i+cutoff
        while j < len(path):
            distance = manhattan(path[i],path[j])
            if distance <= cheat_time:
                count += j - i - distance >= cutoff
                j += 1
            else:
                j += distance - cheat_time
        i += 1
    return count, path

def part2(path):
    cutoff = 100
    cheat_time = 20
    count = 0
    i = 0
    while i < len(path)-cutoff:
        j = i+cutoff
        while j < len(path):
            distance = manhattan(path[i],path[j])
            if distance <= cheat_time:
                count += j - i - distance > cutoff
                j += 1
            else:
                j += distance - cheat_time
        i += 1
    return count

with open("input.txt") as file:
    data = file.read().splitlines()

start = time.perf_counter()
res1, path = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(path)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")