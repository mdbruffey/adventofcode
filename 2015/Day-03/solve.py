def part1(data):
    visited = set()
    i = 0
    j = 0
    visited.add((i,j))
    for char in data:
        if char == "<":
            j -= 1
        elif char == ">":
            j += 1
        elif char == "^":
            i += 1
        else:
            i -= 1
        visited.add((i,j))
    return len(visited)

def part2(data):
    visited = set()
    i = 0
    j = 0
    visited.add((i,j))
    for char in [data[i] for i in range(0,len(data),2)]:
        if char == "<":
            j -= 1
        elif char == ">":
            j += 1
        elif char == "^":
            i += 1
        else:
            i -= 1
        visited.add((i,j))

    i = 0
    j = 0
    for char in [data[i] for i in range(1,len(data),2)]:
        if char == "<":
            j -= 1
        elif char == ">":
            j += 1
        elif char == "^":
            i += 1
        else:
            i -= 1
        visited.add((i,j))
    return len(visited)

with open('input.txt') as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")