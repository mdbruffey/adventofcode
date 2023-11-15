def part1(data):
    floor = 0
    for char in data:
        if char == "(":
            floor += 1
        else:
            floor -= 1

    return floor

def part2(data):
    floor = 0
    for i, char in enumerate(data):
        if char == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i+1

    return 0

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
