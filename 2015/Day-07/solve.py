def get_value(wire, wires):
    operation = wires[wire]
    if operation.isnumeric():
        value = int(operation)
    elif "AND" in operation:
        left, right = operation.split(" AND ")
        if left.isnumeric():
            value = int(left) & get_value(right, wires)
        elif right.isnumeric():
            value = get_value(left, wires) & int(right)
        else:
            value = get_value(left, wires) & get_value(right, wires)
    elif "OR" in operation:
        left, right = operation.split(" OR ")
        if left.isnumeric():
            value = int(left) | get_value(right, wires)
        elif right.isnumeric():
            value = get_value(left, wires) | int(right)
        else:
            value = get_value(left, wires) | get_value(right, wires)
    elif "RSHIFT" in operation:
        left, right = operation.split(" RSHIFT ")
        value = get_value(left, wires) >> int(right)
    elif "LSHIFT" in operation:
        left, right = operation.split(" LSHIFT ")
        value = get_value(left, wires) << int(right)
    elif "NOT" in operation:
        wire = operation.split()[-1]
        value = 65536 + ~get_value(wire, wires)
    else:
        value = get_value(operation, wires)

    wires[wire] = str(value)
    return value

def part1(data):
    wires = {}
    for line in data:
        operation, target = line.split(" -> ")
        wires[target.strip("\n")] = operation
    return get_value("a", wires)

def part2(data, res1):
    wires = {}
    for line in data:
        operation, target = line.split(" -> ")
        wires[target.strip("\n")] = operation
    wires["b"] = str(res1)
    return get_value("a", wires)

with open("input.txt") as file:
    data = file.readlines()


res1 = part1(data)
res2 = part2(data, res1)
print(f"Part 1: {res1}\nPart 2: {res2}")