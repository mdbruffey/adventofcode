import time
import numpy as np
import itertools

def fix_padding(b, length, size):
    for i in range(len(b)):
        if len(b[i]) < 64:
            if i < len(b)-1:
                b[i] = "0"*(64-len(b[i])) + b[i]
            else:
                b[i] = "0"*(length-size-len(b[i])) + b[i]
    return "".join(b)

def extend(a):
    length = len(a)
    a_r = a[::-1]
    b = []
    i = 0
    while len(a_r) > 64:
        b.append(bin(~np.uint64(int(a_r[:64], 2)))[2:])
        a_r = a_r[64:]
        i += 1
    b.append(bin(~np.uint64(int(a_r, 2)))[64-len(a_r)+2:])
    b = fix_padding(b, length, i*64)
    return a+"0"+b

def next(a):
    b = ''.join('0' if c == '1' else '1' for c in reversed(a))
    return ''.join([a, "0", b])

def get_checksum(data):
    checksum = []
    for i in range(0,len(data),2):
        if data[i] == data[i+1]:
            checksum.append("1")
        else:
            checksum.append("0")
    if len(checksum) % 2 != 0:
        return ''.join(checksum)
    else:
        return get_checksum(checksum)

def part1(data, disk_length):
    while len(data) < disk_length:
        print(f"{len(data)}/{disk_length}")
        data = next(data)
    checksum = get_checksum(data[:disk_length])

    return checksum

with open("input.txt") as file:
    data = file.read()

disk_length_1 = 272
disk_length_2 = 35651584

start = time.perf_counter()
res1 = part1(data, disk_length_1)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part1(data, disk_length_2)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")

