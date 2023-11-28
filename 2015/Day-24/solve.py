import math
import time
import itertools

def get_QE(group):
    return math.prod(group)

def make_groups(packages, n):
    total = sum(packages)
    target = total // n
    groups = []
    for i in range(2, len(packages)//n):
        groups.extend(itertools.combinations(packages, i))
    groups = list(filter(lambda x: sum(x)==target, groups))
    return groups

def part1(packages):
    groups = make_groups(packages, 3)
    min_packages = min([len(x) for x in groups])
    shortest = list(filter(lambda x: len(x) == min_packages, groups))
    shortest.sort(key=lambda x: math.prod(x))
    return math.prod(shortest[0])

def part2(data):
    groups = make_groups(packages, 4)
    min_packages = min([len(x) for x in groups])
    shortest = list(filter(lambda x: len(x) == min_packages, groups))
    shortest.sort(key=lambda x: math.prod(x))
    return math.prod(shortest[0])

with open("input.txt") as file:
    data = file.readlines()

packages = set(map(int, data))

start = time.perf_counter()
res1 = part1(packages)
print(f"Part 1: {res1} -- {time.perf_counter() - start:.4f} s")
start = time.perf_counter()
res2 = part2(packages)
print(f"Part 2: {res2} -- {time.perf_counter() - start:.4f} s")