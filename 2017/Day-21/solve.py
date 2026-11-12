import time

starting_cell = [".#.","..#","###"]

def split_cell(cell):
    cells = []
    if len(cell) % 2 == 0:
        w = 2
    else:
        w = 3
    for i in range(0, len(cell), w):
        for j in range(0, len(cell), w):
            new = []
            for k in range(w):
                new.append(cell[i+k][j:j+w])
            cells.append(new)
    return cells

def matches(cell, rule):
    cell = "".join(cell)
    rule = rule[:]
    for _ in range(4):
        if cell == "".join(rule) or cell == "".join([s[::-1] for s in rule]):
            return True
        rule = ["".join([rule[-i-1][j] for i in range(len(rule))]) for j in range(len(rule))]
    return False

def enhance(cell, rules):
    for pattern, result in rules:
        if len(pattern) != len(cell):
            continue
        if matches(cell,pattern):
            return result
    print("uh, oh... No match found")
    print(cell)
    return None

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

def print_cell(cell):
    for line in cell:
        print(" ".join(line))
    print("")

def part1(rules, iterations):
    cell = starting_cell[:]
    for _ in range(iterations):
        cells = split_cell(cell)
        cells = [enhance(c, rules) for c in cells]
        cell = stitch(cells)
    print((len(cell)/3)**2)
    return "".join(cell).count("#")

def get_3x3_evolutions(cell, rules):
    cell = enhance(cell, rules) # -> 4x4
    cells = split_cell(cell) # -> 2x2
    cell = stitch([enhance(c, rules) for c in cells]) #enhancing 2x2s produces a 6x6
    cells = split_cell(cell) # -> into 2x2s again
    return [enhance(c, rules) for c in cells] #return list of resulting 3x3s

def part2(rules):
    evolutions = {}
    cells = {tuple(starting_cell):1}
    for _ in range(6):
        next_cells = {}
        for cell, count in cells.items():
            if cell not in evolutions.keys():
                evolutions[cell] = get_3x3_evolutions(cell, rules)
            for evolves in evolutions[tuple(cell)]:
                next_cells[tuple(evolves)] = next_cells.setdefault(tuple(evolves), 0) + count
        cells = next_cells
    return sum(["".join(key).count("#")*value for key, value in cells.items()])

    

with open("input.txt") as file:
    data = file.read().split("\n")
rules = []
for line in data:
    match, result = line.split(" => ")
    match = match.split("/")
    result = result.split("/")
    rules.append((match, result))

start = time.perf_counter()
res1 = part1(rules, 5)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(rules)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")