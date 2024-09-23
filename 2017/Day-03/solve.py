import time

direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

neighbors = [
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0),
    (-1,-1),
    (0,-1),
    (1,-1)
]

def part1(data):
    n = 1
    x = 0
    y = 0
    dist = 1
    dir = 0
    while True:
        for i in range(2):
            for i in range(dist):
                n += 1
                x += direction[dir%4][0]
                y += direction[dir%4][1]
                if n == data:
                    return x+y
            dir += 1
        dist += 1

def get_cell_value(pos, grid):
    value = 0
    for neighbor in neighbors:
        x = pos[0] + neighbor[0]
        y = pos[1] + neighbor[1]
        if (x,y) in grid:
            value += grid[(x,y)]
    return value

def part2(data):
    grid = {}
    x = 0
    y = 0
    dist = 1
    dir = 0
    grid[(x,y)] = 1
    while True:
        for i in range(2):
            for i in range(dist):
                x += direction[dir%4][0]
                y += direction[dir%4][1]
                value = get_cell_value((x,y), grid)
                if value > data:
                    return value
                grid[(x,y)] = value
            dir += 1
        dist += 1

with open("input.txt") as file:
    data = int(file.readlines()[0])

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")