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

#This is absolutely a brute-force solution...
def fix_update(update, rules):
    while not is_ordered(update, rules):
        for i, num in enumerate(update):
            if num not in rules:
                continue
            pres = [x for x in rules[num] if x in update]
            if pres:
                smallest_i = max([update.index(x) for x in pres])
                if i < smallest_i:
                    update.insert(smallest_i+1, num)
                    update.pop(i)
    return update

def part1(updates, rules):
    val = 0
    for update in updates:
        if is_ordered(update, rules):
            val += update[len(update)//2]
    return val

def part2(updates, rules):
    val = 0
    for update in updates:
        if not is_ordered(update, rules):
            val += fix_update(update, rules)[len(update)//2]
    return val

with open("input.txt") as file:
    data = file.read()

rules, updates = data.split("\n\n")
rules = rules.splitlines()
rules_dict = {}
for rule in rules:
    pre, post = list(map(int,rule.split("|")))
    if post not in rules_dict:
        rules_dict[post] = [pre]
    else:
        rules_dict[post].append(pre)

updates = [list(map(int, line.strip().split(","))) for line in updates.splitlines()]

start = time.perf_counter()
res1 = part1(updates, rules_dict)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(updates, rules_dict)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")