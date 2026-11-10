import time

def knot_hash(string):
    sequence = list(map(ord, string)) + [17, 31, 73, 47, 23]
    ring_length = 256
    ring = tuple(range(ring_length))
    pos = 0
    step = 0
    for _ in range(64):
        for length in sequence:
            start = pos % ring_length
            pos = start
            end = (start + length) % ring_length
            if length == 0 or length == 1:
                pass
            elif start < end:
                ring = ring[:start] + ring[start:end][::-1] + ring[end:]
            elif end == 0:
                ring = ring[:start] + ring[start:][::-1]
            else:
                section = ring[start:] + ring[:end]
                section = section[::-1]
                ring = section[-end:] + ring[end:start] + section[:-end]
            pos += length + step
            step += 1
    dense = []
    for j in range(16):
        val = ring[16*j]
        for i in range(1,16):
            val = val ^ ring[16*j + i]
        dense.append(val)
    
    form = lambda x: f"{x:02x}"
    hash = "".join(map(form,dense))
    return hash

def part1(base):
    form = lambda x: f"{int(x,16):04b}"
    count = 0
    disk = []
    for i in range(128):
        hash = knot_hash(f"{base}-{i}")
        bit_string = "".join(map(form,hash))
        disk.append(bit_string)
        count += bit_string.count("1")
    return count, disk

def get_neighbors(p, disk):
    i, j = p
    neighbors = []
    for x, y in ((1,0), (0,1), (-1,0), (0,-1)):
        if i + x >= 0 and i+x < len(disk) and j + y >=0 and j+y < len(disk):
            if disk[i+x][j+y] == "1":
                neighbors.append((i+x,j+y))
    return neighbors


def traverse(start, disk, traversed):
    queue = [start]
    visited = set()
    while len(queue):
        curr = queue.pop()
        visited.add(curr)
        for neighbor in get_neighbors(curr, disk):
            if neighbor not in visited:
                queue.append(neighbor)
    traversed.update(visited)

def part2(disk):
    traversed = set()
    groups = 0
    for i in range(len(disk)):
        for j in range(len(disk[0])):
            if disk[i][j] == "1" and (i, j) not in traversed:
                traverse((i,j), disk, traversed)
                groups += 1
    return groups

with open("input.txt") as file:
    data = file.read().strip()

start = time.perf_counter()
res1, disk = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(disk)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")