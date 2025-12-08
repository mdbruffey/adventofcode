import time
import math
import heapq

class Junction():
    def __init__(self, coords):
        self.coords = coords
        self.x, self.y, self.z = coords
        self.connected = set((self,))

    def __lt__(self, other):
        return self.x < other.x
    
    def distance(self, other):
        x1,y1,z1 = self.coords
        x2,y2,z2 = other.coords
        return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    
    def connect(self, other):
        if other in self.connected:
            return
        self.connected.update(other.connected)
        for junction in other.connected:
            junction.connected = self.connected

def distance(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def part1(data):
    num_cords = 10 if len(data) < 100 else 1000
    junctions = [Junction(tuple(map(int, line.split(",")))) for line in data]
    distances = []
    for i in range(len(junctions)-1):
        for j in range(i+1, len(junctions)):
            distances.append((junctions[i].distance(junctions[j]),(junctions[i],junctions[j])))
    shortest = heapq.nsmallest(num_cords, distances)
    for j1, j2 in [pair for _,pair in shortest]:
        j1.connect(j2)
    circuits = {}
    for junction in junctions:
        circuit = tuple(sorted(list(junction.connected)))
        if circuit in circuits:
            continue
        circuits[circuit] = len(junction.connected)
    lengths = list(circuits.values())
    lengths.sort(reverse=True)
    return lengths[0]*lengths[1]*lengths[2]

def part2(data):
    junctions = [Junction(tuple(map(int, line.split(",")))) for line in data]
    distances = []
    for i in range(len(junctions)-1):
        for j in range(i+1, len(junctions)):
            distances.append((junctions[i].distance(junctions[j]),(junctions[i],junctions[j])))
    shortest = heapq.nsmallest(10000, distances)
    for j1, j2 in [pair for _,pair in shortest]:
        j1.connect(j2)
        if len(j1.connected) == len(junctions):
            break
    return j1.x*j2.x

with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")