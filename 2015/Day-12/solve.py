def countList(item, p2 = False):
    count = 0
    for item in item:
        if isinstance(item, int):
            count += item
        elif isinstance(item, list):
            count += countList(item, p2)
        elif isinstance(item, dict):
            count += countDict(item, p2)

    return count

def countDict(item, p2 = False):
    if ("red" in item.values() or "red" in item) and p2:
        return 0
    count = 0
    for value in item.values():
        if isinstance(value, int):
            count += value
        elif isinstance(value, list):
            count += countList(value, p2)
        elif isinstance(value, dict):
            count += countDict(value, p2)
    return count

def part1(data):
    thing = eval(data)
    return countList(thing)

def part2(data):
    thing = eval(data)
    return countList(thing, True)

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f'Part 1: {res1}\nPart 2: {res2}')