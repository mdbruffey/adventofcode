import time

starting_cell = [".#.","..#","###"]

def split_cell(cell):
    cells = []
    if len(cell) % 3 == 0:
        w = 3
    else:
        w = 2
    for i in range(0, len(cell), w):
        for j in range(0, len(cell), w):
            new = []
            for k in range(w):
                new.append(cell[i+k][j:j+w])
            cells.append(new)
    return cells

def enhance(cell, rules):
    return cell

def stitch(cells):
    cell = []
    w = len(cells)**0.5
    if not w.is_integer():
        print("uh oh... Don't have enough cells to stitch together a square...")
        return None
    w = int(w)
    for i in range(w):
        row = cells[i*w:(i+1)*w]
        for j in range(len(row[0])):
            cell.append("".join([c[j] for c in row]))
    return cell

def part1(rules):
    cell = starting_cell[:]
    steps = 1
    for _ in range(steps):
        cells = split_cell(cell)
        cells = [enhance(c, rules) for c in cells]
        cell = stitch(cells)
    print(cell)

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read().split("\n")
rules = []
for line in data:
    match, result = line.split(" => ")
    match = match.split("/")
    result = result.split("/")

start = time.perf_counter()
res1 = part1(rules)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(rules)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")