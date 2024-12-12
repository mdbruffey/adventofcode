import time

def has_parent(name, tree):
    dependents = [x["dependents"] for x in tree.values()]
    for row in dependents:
        if row and name in row:
            return True
    return False

def part1(data):
    tree = {}
    for line in data:
        entry = {}
        line = line.split(" -> ")
        name, weight = line[0].split()
        entry["weight"] = int(weight[1:-1])
        if len(line) > 1:
            dependents = line[1].replace("\n","").split(", ")
        else:
            dependents = None
        entry["dependents"] = dependents
        tree[name] = entry
    for key in tree:
        if not has_parent(key, tree):
            return key, tree

def find_bad_disk(weights):
    if weights[0][1] == weights[1][1]:
        bal = weights[0][1]
    elif weights[0][1] == weights[2][1]: #this approach does assume there are at least 3 programs on a disk...
        return weights[1]
    else:
        return weights[0]
    bad = [x for x in weights if x[1] != bal]
    if bad:
        return bad[0]
    return None

def get_weight(name, tree):
    dependents = tree[name]["dependents"]
    weight = tree[name]["weight"]
    if not dependents:
        return weight
    for child in tree[name]["dependents"]:
        weight += get_weight(child, tree)
    return weight

def is_unbalanced(disk, tree):
    weights = []
    for child in tree[disk]["dependents"]:
        weights.append((child,get_weight(child, tree)))
    if weights.count(weights[0]) == len(weights):
        return False
    return weights

def part2(tree, root):
    curr = root
    
    while True:
        weights = is_unbalanced(curr, tree)
        next = find_bad_disk(weights)
        if not next:
            break
        curr = next[0]

    base = is_unbalanced(root, tree)
    bad = find_bad_disk(base)
    base.remove(bad)

    return tree[curr]["weight"] + (base[0][1] - bad[1])

with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1, tree = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(tree, res1)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")