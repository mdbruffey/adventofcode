def execute(operation, target):
    pass

def part1(data):
    wires = {}
    for line in data:
        left, target = line.split(" -> ")
        execute(left, target, wires)
    return wires["a"]

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()


res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")