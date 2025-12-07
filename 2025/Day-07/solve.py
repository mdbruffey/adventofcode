import time

def part1(data):
    beams = set()
    beams.add(data[0].find("S"))
    count = 0
    for i in range(2, len(data), 2):
        split = set()
        for col in beams:
            if data[i][col] == "^":
                split.add(col)
        count += len(split)
        for val in split:
            beams.remove(val)
            beams.update((val-1, val+1))
    return count

def part2(data):
    paths = {}
    top = (data[0].find("S"), 2)
    paths[top] = 1
    row = set((top,))
    for i in range(4, len(data)+1, 2):
        prev = row
        row = set([(j+k, i) for k in [-1,1] for j, _ in prev ])
        for j,i in row:
            left_path = paths.get((j-1, i-2), 0) if data[i-2][j-1] == "^" else 0
            right_path = paths.get((j+1, i-2), 0) if data[i-2][j+1] == "^" else 0
            center_path = paths.get((j, i-4), 0) if data[i-4][j] == "." else 0
            paths[(j,i)] = left_path + center_path + right_path
    return sum([paths[pos] for pos in row]) + sum([paths[pos] for pos in prev if data[pos[1]][pos[0]] == "."])

def part2_v2(data):
    beams = {}
    for i in range(len(data[0])):
        beams[i] = 0
    beams[data[0].find("S")] = 1
    for i in range(2, len(data), 2):
        for j in range(len(data[i])):
            if data[i][j] == "^":
                beams[j-1] += beams[j]
                beams[j+1] += beams[j]
                beams[j] = 0
    return sum(beams.values())


with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res3 = part2_v2(data)
print(f"Part 2 v.2: {res3} -- {time.perf_counter()-start:.4f} s")