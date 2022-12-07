def part1(data):
    
    def masked(val, mask):
        zero = []
        one = []
        for i in range(1,len(mask)+1):
            if mask[-i] == "0":
                zero.append(i)
            elif mask[-i] == "1":
                one.append(i)
        bits = to_bits(val)
        for index in zero:
            bits[-index] = "0"
        for index in one:
            bits[-index] = "1"
        val = to_int(bits)
        return val

    def to_bits(val):
        bit = bin(int(val))
        bit = bit[2:]
        bit = [c for c in bit]
        bits = ["0" for i in range(36-len(bit))]
        bits.extend(bit)
        return bits

    def to_int(bits):
        val = int("0b" + "".join(bits),2)
        return val

    
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

    def masked(val, mask):
        x = []
        one = []
        for i in range(1,len(mask)+1):
            if mask[-i] == "X":
                x.append(i)
            elif mask[-i] == "1":
                one.append(i)
        bits = to_bits(val)
        for index in x:
            bits[-index] = "X"
        for index in one:
            bits[-index] = "1"
        vals = get_floating_addresses("0b" + "".join(bits))
        #print("---------------------\n",vals)
        return list(map(lambda x: int(x,2),vals))

    def get_floating_addresses(bits):
        local_vals = []
        vals = []
        #print(bits)
        if "X" not in bits:
            return [int(bits,2)]
        index = bits.find("X")
        local_vals.append(bits[:index] + "0" + bits[index+1:])
        local_vals.append(bits[:index] + "1" + bits[index+1:])
        for val in local_vals:
            #print(val)
            if "X" in val:
                vals.extend(get_floating_addresses(val))
            else:
                vals.append(val)
        return vals

    def to_bits(val):
        bit = bin(int(val))
        bit = bit[2:]
        bit = [c for c in bit]
        bits = ["0" for i in range(36-len(bit))]
        bits.extend(bit)
        return bits

    data = data.split("\n")
    mem = {}
    for line in data:
        ins, val = line.split(" = ")
        if ins == "mask":
            mask = val
        else:
            loc = ins[ins.find("[")+1:-1]
            locs = masked(loc, mask)
            for loc in locs:
                mem[loc] = int(val)

    return sum([mem[loc] for loc in mem.keys()])
    
with open("input.txt") as file:
    data = file.read()

res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")
