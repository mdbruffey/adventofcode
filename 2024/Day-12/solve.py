import time

directions = {(1,0),(0,1),(-1,0),(0,-1)}

#I borrowed this from somebody. I have no idea how it works, but it does count corners/sides properly.
def count_sides(region):
    corners, double = set(), 0
    xs, ys = set(x for y,x in region), set(y for y,x in region)
    for y in range(min(ys), max(ys)+2):
        for x in range(min(xs), max(xs)+2):
            index = sum(((y+dy,x+dx) in region)*sf 
                            for dx,dy,sf in [(-1,-1,1),(-1,0,2),(0,-1,4),(0,0,8)])
            if index not in [0,3,5,10,12,15]: corners.add((y,x))
            if index in [6, 9]: double += 1
    return len(corners)+double


def part1(data):
    visited = set()
    cost = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            start = (j, i)
            if start in visited:
                continue
            sides = 0
            area = 0
            queue = [start]
            while queue:
                curr = queue.pop(0)
                area += 1
                visited.add(curr)
                x,y = curr
                for dx, dy in directions:
                    next = (x+dx,y+dy)
                    if 0 <= x+dx < len(data[0]) and 0 <= y+dy < len(data):
                        if data[y][x] == data[y+dy][x+dx]:
                            if next not in visited and next not in queue:
                                queue.append(next)
                        else:
                            sides += 1
                    else:
                        sides += 1
            cost += area*sides
    return cost
                

def part2(data):
    visited = set()
    cost = 0
    regions = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            start = (j, i)
            if start in visited:
                continue
            region = []
            queue = [start]
            while queue:
                curr = queue.pop(0)
                region.append(curr)
                visited.add(curr)
                x,y = curr
                for dx, dy in directions:
                    next = (x+dx,y+dy)
                    if 0 <= x+dx < len(data[0]) and 0 <= y+dy < len(data):
                        if (data[y][x] == data[y+dy][x+dx]
                            and next not in visited and next not in queue):
                                queue.append(next)
            cost += len(region)*count_sides(region)

    return cost

with open("input.txt") as file:
    data = file.read().splitlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")