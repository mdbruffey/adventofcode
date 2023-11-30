import time

def get_neighbors(coord, desig):
    x, y, steps = coord
    steps += 1
    neighbors = [(x,y-1, steps),(x+1,y, steps),(x,y+1, steps),(x-1,y, steps)]
    neighbors = [coord for coord in neighbors if coord[0] >= 0 and coord[1] >= 0]
    return [coord for coord in neighbors if not is_wall(coord[:-1], desig)]

def is_wall(coord, d_num):
    x,y = coord
    num = (x**2 + 3*x + 2*x*y + y + y**2) + d_num
    if format(num, 'b').count("1") % 2 == 0:
        return False
    return True

def part1(data):
    coord = (1,1,0)
    target = (31,39)
    queue = [coord]
    visited = set()
    while queue:
        coord = queue.pop(0)
        if coord[:-1] == target:
            return coord[-1]
        for next in get_neighbors(coord, data):
            if next[:-1] not in visited:
                queue.append(next)
                visited.add(next[:-1])

def part2(data):
    coord = (1,1,0)
    queue = [coord]
    visited = set()
    while True:
        coord = queue.pop(0)
        if coord[-1] > 49:
            return len(visited)
        for next in get_neighbors(coord, data):
            if next[:-1] not in visited:
                queue.append(next)
                visited.add(next[:-1])

with open("input.txt") as file:
    data = int(file.read())

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")