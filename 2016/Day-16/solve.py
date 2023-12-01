import time
import numpy as np

def extend(a):
    length = len(a)
    try:
        if length > 128:
            b = []
            a_r = a[::-1]
            print(a_r)
            b.append(bin(~np.uint64(int(a_r[:64], 2)))[2:])
            b.append(bin(~np.uint64(int(a_r[64:128], 2)))[2:])
            b.append(bin(~np.uint64(int(a_r[128:], 2)))[192-length +2:])
            for i in range(len(b)):
                if len(b[i]) < 64:
                    if i < len(b)-1:
                        b[i] = "0"*(64-len(b[i])) + b[i]
                    else:
                        b[i] = "0"*(length-128-len(b[i])) + b[i]
            b = "".join(b)
            print(b)
        elif length > 64:
            a_r = a[::-1]
            b = bin(~np.uint64(int(a_r[:64], 2)))[2:] + bin(~np.uint64(int(a_r[64:], 2)))[128-length+2:]
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

def part2(data):
    pass

with open("input.txt") as file:
    data = file.read()

disk_length = 20

thing = "0"*63 + "1" + "0" + "1"*65

extend(thing)

start = time.perf_counter()
#res1 = part1(data, disk_length)
#print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(data)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")

