def part1(data):
    def masked(val, mask):
        zero = []
        one = []
        for i in range(1,len(mask)-1):
            if mask[-i] == "0":
                zero.append(i)
            elif mask[-i] == "1":
                one.append(i)
        print(zero,one)
        val = int(val).
        print(f"Before mask: {val}")
        for index in zero:
            val & ~(1 << index)
        for index in one:
            val | (1 << index)
        print(f"After mask: {val}")
    
    data = data.split("\n")
    mem = {}
    for line in data:
        ins, val = line.split(" = ")
        if ins == "mask":
            mask = val
        else:
            loc = ins[ins.find("[")+1:-1]
            mem[loc] = masked(val, mask)
    return sum([mem[loc] for loc in mem.keys()])

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
