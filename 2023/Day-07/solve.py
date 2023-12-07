import time

def sort(hands):
    pass

def part1(hands):
    hands = sort(hands)
    count = 0
    for i in range(len(hands)):
        count += (i+1)*hands[i][1]
    return count

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()

hands = []

for line in data:
    hand, bid = line.strip("\n").split()
    bid = int(bid)
    hands.append([hand, bid])

start = time.perf_counter()
res1 = part1(hands)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(hands)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")