import time

def next_term(seq):
    seqs = [seq]
    while seqs[-1].count(0) != len(seqs[-1]):
        curr = seqs[-1]
        next = []
        for i in range(len(curr)-1):
            next.append(curr[i+1]-curr[i])
        seqs.append(next)
    return sum(x[-1] for x in seqs)

def prev_term(seq):
    seqs = [seq]
    while seqs[-1].count(0) != len(seqs[-1]):
        curr = seqs[-1]
        next = []
        for i in range(len(curr)-1):
            next.append(curr[i+1]-curr[i])
        seqs.append(next)
    nums = [x[0] for x in seqs]
    count = 0
    for i in range(len(nums)-1,-1,-1):
        count = nums[i] - count
    return count


def part1(seqs):
    return sum(map(next_term, seqs))

def part2(seqs):
    return sum(map(prev_term, seqs))

with open("input.txt") as file:
    data = file.read()

data = data.split("\n")
seqs = []
for line in data:
    seq = list(map(int, line.split()))
    seqs.append(seq)

start = time.perf_counter()
res1 = part1(seqs)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(seqs)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")