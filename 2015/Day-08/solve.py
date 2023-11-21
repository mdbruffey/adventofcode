def encoded_length(string):
    count = len(string) + 2
    for char in string:
        if char in "\"\\":
            count += 1
    return count

def part1(data):
    full_count = 0
    mem_count = 0
    for line in data:
        full_count += len(line)
        mem_count += len(eval(line))
    return full_count - mem_count

def part2(data):
    full_count = 0
    enc_count = 0
    for line in data:
        full_count += len(line)
        enc_count += encoded_length(line)
    return enc_count - full_count

with open("input.txt") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].strip("\n")
res1 = part1(data)
res2 = part2(data)
print(f"Part 1: {res1}\nPart 2: {res2}")