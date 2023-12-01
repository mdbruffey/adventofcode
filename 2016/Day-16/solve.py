import time
import numpy as np

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
    try:
        if length > 128:
            a_r = a[::-1]
            b = []
            b.append(bin(~np.uint64(int(a_r[:64], 2)))[2:])
            b.append(bin(~np.uint64(int(a_r[64:128], 2)))[2:])
            b.append(bin(~np.uint64(int(a_r[128:], 2)))[192-length +2:])
            b = fix_padding(b, length, 128)
        elif length > 64:
            a_r = a[::-1]
            b= []
            b.append(bin(~np.uint64(int(a_r[:64], 2)))[2:])
            b.append(bin(~np.uint64(int(a_r[64:], 2)))[128-length+2:])
            b = fix_padding(b, length, 64)
        elif length > 32:
            b = bin(~np.uint64(int(a[::-1], 2)))[64-length+2:]
        else:
            b = bin(~np.uint32(int(a[::-1], 2)))[32-length+2:]
    except Exception as e:
        print(e)
        print(len(a))

    return a+"0"+b

def get_checksum(data):
    checksum = ""
    for i in range(0,len(data),2):
        if data[i] == data[i+1]:
            checksum += "1"
        else:
            checksum += "0"
    return checksum

def part1(data, disk_length):
    while len(data) < disk_length:
        data = extend(data)
    checksum = get_checksum(data[:disk_length])
    while len(checksum) % 2 == 0:
        checksum = get_checksum(checksum)

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

