import time

def part1(data):
    l1 = []
    l2 = []
    for line in data:
        nums = list(map(int,line.split()))
        l1.append(nums[0])
        l2.append(nums[1])
    l1.sort()
    l2.sort()
    count = 0
    for i in range(len(l1)):
        count += abs(l1[i]-l2[i])
    return count

def part2(data):
    l1 = []
    l2 = []
    for line in data:
        nums = list(map(int,line.split()))
        l1.append(nums[0])
        l2.append(nums[1])
    l1.sort()
    l2.sort()
    count = 0
    for i in range(len(l1)):
        count += l1[i]*l2.count(l1[i])
    return count

with open("input.txt") as file:
    data = file.read()
    data = data.splitlines()



start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")