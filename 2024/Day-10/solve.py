import time

def get_neighbors(pos, data):
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    x,y = pos
    neighbors = []
    for dir in directions:
        dx,dy = dir
        if x+dx < 0 or y + dy < 0 or x+dx >= len(data[0]) or y+dy >= len(data):
            continue
        if int(data[y+dy][x+dx]) - int(data[y][x]) == 1:
            neighbors.append((x+dx,y+dy))
    return neighbors

def part1(data):
    heads = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "0":
                heads.append((x,y))
    count = 0
    paths = 0
    for head in heads:
        queue = [head]
        peaks = set()
        while len(queue) > 0:
            curr = queue.pop()
            x,y = curr
            if data[y][x] == "9":
                peaks.add(curr)
                paths += 1 #pretty sure this gets the result for part 2
            else:
                queue.extend(get_neighbors(curr, data))
        count += len(peaks)
    return count, paths

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read().splitlines()

start = time.perf_counter()
res1, res2 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
#res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")