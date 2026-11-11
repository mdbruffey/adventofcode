import time
import numpy as np

def calc_position(t, p0, v0, a):
    return .5*a*t**2 + v0*t + p0

def part1(particles):
    time = 10000
    lowest = 1000000000000000000000000000
    lowest_id = -1
    for p in particles:
        pos = calc_position(time, p["p"], p["v"], p["a"])
        magn = np.linalg.norm(pos)
        if  magn < lowest:
            lowest = magn
            lowest_id = p["id"]
    return lowest_id

def part2(particles):
    finished = 0
    while True:
        #tick
        occupied = set()
        to_remove = set()
        to_keep = []
        changed = 0
        #update positions, identify all unique positions and which particle positions to remove
        for p in particles:
            p["v"] += p["a"]
            p["p"] += p["v"]
            if tuple(p["p"]) in occupied:
                to_remove.add(tuple(p["p"]))
            else:
                occupied.add(tuple(p["p"]))
        #remove all positions that multiple particles occupy after the step
        occupied.difference_update(to_remove)
        #now remove all particles whose position is not in the occupied step (they collided)
        if len(to_remove):
            for p in particles:
                if tuple(p["p"]) in occupied:
                    to_keep.append(p)
            changed = len(to_keep) - len(particles)
            particles = to_keep
        #try to decide if we need to keep going or not
        if changed == 0:
            finished += 1
        else:
            finished = 0
        #I figure if we've made it 20 cycles with no collisions, we're probably good
        if finished == 20:
            break
    return len(particles)

with open("input.txt") as file:
    data = file.read().split("\n")
particles = []
for i, line in enumerate(data):
    p, v, a = line.split(", ")
    p = np.array(list(map(int, p.split("=<")[1][:-1].split(","))))
    v = np.array(list(map(int, v.split("=<")[1][:-1].split(","))))
    a = np.array(list(map(int, a.split("=<")[1][:-1].split(","))))
    particles.append({"p": p, "v": v, "a": a, "id": i})

start = time.perf_counter()
res1 = part1(particles)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(particles)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")