import time
import numpy as np

unit_vectors = {0: np.array([1,0]),
                90: np.array([0,1]),
                180: np.array([-1,0]),
                270: np.array([0,-1])}

def part1(data):
    pos = np.array([0,0])
    direction = 0
    for instruction in data:
        if instruction[0] == "L":
            direction += 90
        else:
            direction -= 90
        if direction < 0:
            direction += 360
        if direction > 270:
            direction -= 360
        pos += int(instruction[1:])*unit_vectors[direction]

    return abs(pos[0]) + abs(pos[1])

def part2(data):
    pos = np.array([0,0])
    visited = []
    direction = 0
    for instruction in data:
        if instruction[0] == "L":
            direction += 90
        else:
            direction -= 90
        if direction < 0:
            direction += 360
        if direction > 270:
            direction -= 360
        for i in range(int(instruction[1:])):
            pos += unit_vectors[direction]
            if list(pos) not in visited:
                visited.append(list(pos))
            else:
                return abs(pos[0]) + abs(pos[1])

with open("input.txt") as file:
    data = file.read()

data = data.split(", ")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")