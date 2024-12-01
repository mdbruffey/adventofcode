import time

def has_parent(name, tree):
    for dependents in tree.values():
        if dependents and name in dependents:
            return True
    return False

def part1(data):
    tree = {}
    for line in data:
        line = line.split(" -> ")
        name = line[0].split()[0]
        if len(line) > 1:
            dependents = line[1].replace("\n","").split(", ")
        else:
            dependents = None
        tree[name] = dependents
    for key in tree:
        if not has_parent(key, tree):
            return key

def get_children_weight(name, tree):
    dependents = tree[name]["dependents"]
    weight = 0
    if not dependents:
        return weight
    for child in tree[name]["dependents"]:
        weight += tree[child]["weight"] + get_children_weight(child, tree)
    return weight

def is_unbalanced(disk, tree):
    weights = []
    for child in tree[disk]["dependents"]:
        weights.append(tree[child]['weight'] + get_children_weight(child, tree))
    if weights.count(weights[0]) == len(weights):
        return False
    return weights

def part2(data, root):
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
    
    for dependent in tree["tknk"]["dependents"]:
        print(f"{dependent}: {tree[dependent]['weight'] + get_children_weight(dependent, tree)}")
    print(f"{root} balanced: {not is_unbalanced(root, tree)}")
    return tree["tknk"]['weight'] + get_children_weight("tknk",tree)
with open("input.txt") as file:
    data = file.readlines()

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data, res1)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")