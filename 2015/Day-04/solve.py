import hashlib

def part1(key):
    i = 1
    while True:
        result = hashlib.md5((key+str(i)).encode())
        if result.hexdigest()[:5] == "00000":
            return i
        i += 1

def part2(key):
    i = 1
    while True:
        result = hashlib.md5((key+str(i)).encode())
        if result.hexdigest()[:6] == "000000":
            return i
        i += 1

with open("input.txt") as file:
    key = file.read()

res1 = part1(key)
res2 = part2(key)
print(f"Part 1: {res1}\nPart 2: {res2}")