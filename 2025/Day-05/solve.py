import time

def is_fresh(ingredient, ranges):
    for range in ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            return True
    return False

def part1(data):
    ranges, ingredients = data
    ranges = [list(map(int, line.split("-"))) for line in ranges]

    count = 0
    for ingredient in ingredients:
        count += is_fresh(int(ingredient), ranges)
    return count

def part2(data):
    ranges = [list(map(int, line.split("-"))) for line in data[0]]
    ranges.sort(key=lambda x: x[0])

    count = ranges[0][1] -  ranges[0][0] + 1
    largest = ranges[0][1]
    for i in range(1, len(ranges)):
        if ranges[i][0] <= largest and ranges[i][1] <= largest:
            continue
        count += ranges[i][1] -  ranges[i][0] + 1
        if ranges[i][0] <= largest:
            count -= largest - ranges[i][0] + 1
        if ranges[i][1] > largest:
            largest = ranges[i][1]
    return count



with open("input.txt") as file:
    data = file.read().split("\n\n")

data = [x.split("\n") for x in data]

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.5f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.5f} s")