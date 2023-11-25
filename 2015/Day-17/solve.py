import random

def distribute_eggnog(buckets):
    while True:
        filled = []
        while sum([buckets[i] for i in filled])<150:
            filled = random_bucket(filled, len(buckets))
        if sum([buckets[i] for i in filled]) == 150:
            filled.sort()
            return filled

def random_bucket(filled, num_buckets):
    while True:
        bucket = random.randint(0,num_buckets-1)
        if bucket not in filled:
            filled.append(bucket)
            return filled

def part1(buckets):
    perms = []
    for i in range(100000):
        fill = distribute_eggnog(buckets)
        if fill not in perms:
            perms.append(fill)
    return perms

def part2(combinations):
    fewest = min(len(x) for x in combinations)
    count = 0
    for combo in combinations:
        if len(combo) == fewest:
            count += 1
    return count

with open("input.txt") as file:
    data = file.readlines()

buckets = []
for line in data:
    line = line.strip("\n")
    buckets.append(int(line))

combinations = part1(buckets)
res1 = len(combinations)
res2 = part2(combinations)
print(f"Part 1: {res1}\nPart 2: {res2}")