import time

def part1(seeds):
    a, b = seeds
    count = 0
    for i in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        if a & 65535 == b & 65535:
            count += 1
    return count

def part2(seeds):
    a, b = seeds
    count = 0
    for i in range(5000000):
        a = (a * 16807) % 2147483647
        while a % 4 != 0:
            a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        while b % 8 != 0:
            b = (b * 48271) % 2147483647
        if a & 65535 == b & 65535:
            count += 1
    return count

with open("input.txt") as file:
    data = file.read().split("\n")
seeds = [int(data[0].split()[-1]), int(data[1].split()[-1])]

start = time.perf_counter()
res1 = part1(seeds)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(seeds)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")