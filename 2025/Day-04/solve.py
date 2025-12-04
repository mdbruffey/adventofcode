import time
from collections import deque

def get_neighbors(loc, data):
    x, y = loc
    neighbors = []
    for dy in range(-1,2):
        for dx in range(-1,2):
            if x+dx >= 0 and y+dy >= 0 and x+dx < len(data[y]) and y+dy < len(data):
                if data[y+dy][x+dx] == "@" and (dx != 0 or dy != 0):
                    neighbors.append((x+dx, y+dy))
    return neighbors

def print_graph(data):
    for line in data:
        print(line)
    print()

def part1(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@" and len(get_neighbors((j,i), data)) < 4:
                count += 1
    return count

def part2(data):
    to_remove = deque()
    remove_set = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@" and len(get_neighbors((j,i), data)) < 4:
                to_remove.append((j,i))
                remove_set.add((j,i))
    count = 0
    while len(to_remove):
        j,i = to_remove.pop()
        data[i] = data[i][:j] + "." + data[i][j+1:]
        count += 1
        for neighbor in get_neighbors((j,i), data):
            if neighbor not in remove_set and len(get_neighbors(neighbor, data)) < 4:
                to_remove.append(neighbor)
                remove_set.add(neighbor)
    return count

with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")