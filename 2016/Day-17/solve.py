import time
import hashlib

HEIGHT = 4
WIDTH = 4

def get_moves(curr, key):
    unlocked = "bcdef"
    
    moves = []
    hash = hashlib.md5((key+curr[0]).encode()).hexdigest()[:4]
    for i in range(len(hash)):
        path = curr[0]
        x, y = curr[1]
        if hash[i] in unlocked:
            if i == 0 and y-1 >= 0:
                path += "U"
                y -= 1
            elif i == 1 and y+1 < HEIGHT:
                path += "D"
                y += 1
            elif i == 2 and x-1 >= 0:
                path += "L"
                x -= 1
            elif i == 3 and x+1 < WIDTH:
                path += "R"
                x += 1
            else:
                continue
            moves.append((path,(x,y)))
    return moves

def part1(key):
    queue = [("", (0,0))]
    visited = set()
    while queue:
        curr = queue.pop(0)
        if curr[1] == (3,3):
            return curr[0]
        for move in get_moves(curr, key):
            if move not in visited:
                queue.append(move)
                visited.add(move)

    return "crap"

def part2(key):
    queue = [("", (0,0))]
    visited = set()
    accessed = set()
    while queue:
        curr = queue.pop(0)
        if curr[1] == (3,3):
            accessed.add(curr)
            continue
        for move in get_moves(curr, key):
            if move not in visited:
                queue.append(move)
                visited.add(move)

    return max([len(path[0]) for path in accessed])

with open("input.txt") as file:
    key = file.read()

start = time.perf_counter()
res1 = part1(key)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(key)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")