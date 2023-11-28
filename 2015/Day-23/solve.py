def part1(data):
    i = 0
    registers = {"a": 0,
                 "b": 0}
    while i < len(data):
        inst = data[i]
        op = inst[0]
        if op == "inc":
            registers[inst[1]] += 1
            i += 1
        elif op == "tpl":
            registers[inst[1]] *= 3
            i += 1
        elif op == "hlf":
            registers[inst[1]] //= 2
            i += 1
        elif op == "jmp":
            i += int(inst[1])
        elif op == "jio":
            if registers[inst[1]] == 1:
                i += inst[2]
            else:
                i += 1
        elif op == "jie":
            if registers[inst[1]] % 2 == 0:
                i += inst[2]
            else:
                i += 1
        else:
            print(f"Something went wrong? -- Instruction: {inst}")
            break
    return registers["b"]

def part2(data):
    i = 0
    registers = {"a": 1,
                 "b": 0}
    while i < len(data):
        inst = data[i]
        op = inst[0]
        if op == "inc":
            registers[inst[1]] += 1
            i += 1
        elif op == "tpl":
            registers[inst[1]] *= 3
            i += 1
        elif op == "hlf":
            registers[inst[1]] //= 2
            i += 1
        elif op == "jmp":
            i += int(inst[1])
        elif op == "jio":
            if registers[inst[1]] == 1:
                i += inst[2]
            else:
                i += 1
        elif op == "jie":
            if registers[inst[1]] % 2 == 0:
                i += inst[2]
            else:
                i += 1
        else:
            print(f"Something went wrong? -- Instruction: {inst}")
            break
    return registers["b"]

with open("input.txt") as file:
    data = file.readlines()
instructions = []
for line in data:
    line = line.strip("\n").split()
    if len(line) == 3:
        line[1] = line[1].strip(",")
        line[2] = int(line[2])
    instructions.append(line)

res1 = part1(instructions)
print(f"Part 1: {res1}")
res2 = part2(instructions)
print(f"Part 2: {res2}")