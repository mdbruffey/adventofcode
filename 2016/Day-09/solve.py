import time
from itertools import takewhile, islice

#my recursive solution (really slow, lol)
def get_decompressed_length(data):
    decompressed = 0
    i = 0
    while i < len(data):
        if data[i] == "(":
            marker = ""
            i += 1
            while data[i] != ")":
                marker += data[i]
                i += 1
            seg_length, repeat = list(map(int, marker.split("x")))
            segment = data[i+1:i+1+seg_length]
            if "(" not in segment:
                decompressed += len(segment)*repeat
                data = data[i+1+seg_length:]
                i = 0
            else:
                decompressed += get_decompressed_length(segment*repeat)
                data = data[i+1+seg_length:]
                i = 0
        else:
            decompressed += 1
            i += 1

    return decompressed

#u/barnybug's recursive solution using iter() and itertools
def decompress(data):
    length = 0
    chars = iter(data)
    for c in chars:
        if c == "(":
            n, m = map(int, ["".join(takewhile(lambda c: c not in "x)", chars)) for _ in (0,1)])
            s = "".join(islice(chars, n))
            length += decompress(s)*m
        else:
            length += 1

    return length

def part1(data):
    i = 0
    decompressed = ""
    while i < len(data):
        if data[i] == "(":
            marker = ""
            i += 1
            while data[i] != ")":
                marker += data[i]
                i += 1
            seg_length, repeat = list(map(int, marker.split("x")))
            i += 1
            segment = data[i:i+seg_length]
            decompressed += segment*repeat
            i += seg_length
        else:
            decompressed += data[i]
            i += 1
    return len(decompressed)

def part2(data):
    return decompress(data)

with open("input.txt") as file:
    data = file.read().replace(" ","")

start = time.perf_counter()
res1 = part1(data)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")