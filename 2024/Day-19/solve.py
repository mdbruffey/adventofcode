import time

cache = {}
#I had to look at someone's solution to understand how to make this recursive.
#Kind of stupidly, I was already sort of doing this with basically a pathfinding algorithm, lol
#I did implement the memoization myself, though, so at least I didn't just copy everything
#Part 1 takes the longest because it does all the hard work, then Part 2 is super fast.
def find_possibilities(pattern, towels): 
    count = 0
    if len(pattern) == 0:
        return 1
    for towel in towels:
        if pattern.find(towel) == 0:
            next = pattern[len(towel):]
            if next in cache:
                count += cache[next]
            else:
                result = find_possibilities(next, towels)
                cache[next] = result
                count += result
    return count

def part1(towels, patterns):
    possible = set()
    for pattern in patterns:
        if find_possibilities(pattern, towels) > 0:
            possible.add(pattern)
    return len(possible), possible


def part2(towels, patterns):
    count = 0
    for pattern in patterns:
        count += find_possibilities(pattern, towels)
    return count

with open("input.txt") as file:
    data = file.read()
towels, patterns = data.split("\n\n")
towels = towels.split(", ")
print(len(towels))
patterns = patterns.splitlines()

start = time.perf_counter()
res1, possible = part1(towels, patterns)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(towels, possible)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")