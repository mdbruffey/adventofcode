import time

def part1(data):
    return sum(list(map(int, data)))

def part2(data):
    seen = set((0,))
    freq = 0
    nums = list(map(int, data))
    while True:
        for num in nums:
            freq += num
            if freq not in seen:
                seen.add(freq)
            else:
                return freq

with open("input.txt") as file:
    data = file.read().split("\n")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")