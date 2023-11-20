def execute(operation, target, wires):
    print(operation)
    if operation.isnumeric():
        wires[target] = int(operation)
    elif "AND" in operation:
        left, right = operation.split(" AND ")
        wires[target] = wires[left] & wires[right]
    elif "OR" in operation:
        left, right = operation.split(" OR ")
        wires[target] = wires[left] | wires[right]
    elif "RSHIFT" in operation:
        left, right = operation.split(" RSHIFT ")
        wires[target] = wires[left] >> int(right)
    elif "LSHIFT" in operation:
        left, right = operation.split(" LSHIFT ")
        wires[target] = wires[left] << int(right)
    elif "NOT" in operation:
        wire = operation.split()[-1]
        wires[target] = 65536 + ~wires[wire]
    return wires

def part1(data):
    wires = {}
    for line in data:
        left, target = line.split(" -> ")
        wires = execute(left, target.strip("\n"), wires)
    print(wires)
    return wires["x"]

def part2(data):
    pass

with open("input.txt") as file:
    data = file.readlines()


res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")