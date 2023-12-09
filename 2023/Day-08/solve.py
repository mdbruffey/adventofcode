import time
import math

def loop_length(directions, start, nodes):
    i = 0
    curr = start
    while True:
        idx = 0 if directions[i%len(directions)] == "L" else 1
        next = nodes[curr][idx]
        if next[-1] == "Z":
            return i+1
        curr = next
        i += 1

def part1(directions, nodes):
    return loop_length(directions, "AAA", nodes)       

def part2(directions, nodes):
    curr = [x for x in nodes if "A" == x[-1]]
    periods = []
    for node in curr:
        periods.append(loop_length(directions, node, nodes))
    return math.lcm(*periods)

with open("input.txt") as file:
    data = file.read()

directions, data = data.split("\n\n")
data = data.split("\n")
nodes = {}
for line in data:
    node, neighbors = line.split(" = ")
    neighbors = neighbors.strip(")(").split(", ")
    nodes[node] = neighbors

start = time.perf_counter()
res1 = part1(directions, nodes)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(directions, nodes)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")
