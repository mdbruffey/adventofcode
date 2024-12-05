import time

def is_ordered(update, rules):
    for i,num in enumerate(update):
        if num not in rules:
            continue
        pres = rules[num]
        for pre in pres:
            if pre in update[i:]:
                return False
    return True

#I feel like there's probably a more efficient algorithm...
def fix_update(update, rules):
    fixed = False
    while not fixed:
        fixed = True
        for i, num in enumerate(update):
            if num not in rules:
                continue
            pres = [x for x in rules[num] if x in update]
            if pres:
                smallest_i = max([update.index(x) for x in pres])
                if i < smallest_i:
                    update.insert(smallest_i+1, num)
                    update.pop(i)
                    fixed = False
    return update

def part1(updates, rules):
    val = 0
    broken = []
    for update in updates:
        if is_ordered(update, rules):
            val += update[len(update)//2]
        else:
            broken.append(update)
    return val, broken #decided to send the list of broken updates back since part 2 only needs those

def part2(broken, rules):
    val = 0
    for update in broken:
        val += fix_update(update, rules)[len(update)//2]
    return val

with open("input.txt") as file:
    data = file.read()

rules, updates = data.split("\n\n")
rules = rules.splitlines()
rules_dict = {}
for rule in rules:
    pre, num = list(map(int,rule.split("|")))
    rules_dict[num] = rules_dict.get(num, []) + [pre]

updates = [list(map(int, line.strip().split(","))) for line in updates.splitlines()]

start = time.perf_counter()
res1, broken = part1(updates, rules_dict)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(broken, rules_dict)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")