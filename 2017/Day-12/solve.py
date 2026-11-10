import time

def part1(programs):
    queue = [0]
    visited = set()
    while len(queue):
        curr = queue.pop()
        visited.add(curr)
        for connected in programs[curr]:
            if connected not in visited and connected not in queue:
                queue.append(connected)
    return len(visited)


def part2(data):
    groups = 0
    visited = set()
    for i in range(len(data)):
        if i not in visited:
            queue = [i]
            while len(queue):
                curr = queue.pop()
                visited.add(curr)
                for connected in programs[curr]:
                    if connected not in visited and connected not in queue:
                        queue.append(connected)
            groups += 1
    return groups

with open("input.txt") as file:
    data = file.readlines()
programs = {}    
for line in data:
    line = line.strip().split(" <-> ")
    id, connected = int(line[0]), list(map(int,line[1].split(", ")))
    programs[id] = connected

start = time.perf_counter()
res1 = part1(programs)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")