import time

def part1(data):
    count = 0
    for card in data:
        i = 0
        for num in [int(x) for x in card["nums"] if x.isnumeric()]:
            if num in [int(x) for x in card["wins"] if x.isnumeric()]:
                i += 1
        if i > 0:
            count += 2**(i-1)

    return count
        

def part2(data):
    counts = [1 for i in range(len(data))]
    for i, card in enumerate(data):
        wins = 0
        for num in [int(x) for x in card["nums"] if x.isnumeric()]:
            if num in [int(x) for x in card["wins"] if x.isnumeric()]:
                wins += 1
        if wins > 0:
            if i + wins >= len(counts)-1:
                end = len(counts)
            else:
                end = i+wins+1
            for j in range(i+1, end):
                counts[j] += counts[i]

    return sum(counts)

with open("input.txt") as file:
    data = file.readlines()

cards = []

for line in data:
    card = {}
    line = line.strip("\n")
    id, nums = line.split(": ")
    wins, nums = nums.split(" | ")
    card["id"] = id
    card["wins"] = wins.split()
    card["nums"] = nums.split()
    cards.append(card)
    

start = time.perf_counter()
res1 = part1(cards)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(cards)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")